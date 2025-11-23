from isaaclab.utils import configclass
from isaaclab.envs.mimic_env_cfg import MimicEnvCfg, SubTaskConfig
import isaaclab.sim as sim_utils
from isaaclab.sensors import TiledCameraCfg, FrameTransformerCfg, OffsetCfg

from .pick_orange_mimic_env_cfg import PickOrangeMimicEnvCfg
from leisaac.assets.robots.omx_robot import OMX_ROBOT_CFG


@configclass
class PickOrangeOMXMimicEnvCfg(PickOrangeMimicEnvCfg):
    """
    Configuration for the pick orange task with mimic environment and OMX robot.
    """

    def __post_init__(self):
        super().__post_init__()
        
        # Override robot
        self.scene.robot = OMX_ROBOT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # Override ee_frame to use correct link (omx_f/link0 is the base)
        # Use link5 as the target frame because end_effector_link is not a rigid body
        # Add two target frames to match SO101 structure: gripper (index 0) and jaw (index 1)
        self.scene.ee_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/omx_f/link0",
            debug_vis=False,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/omx_f/link5",
                    name="gripper",
                    offset=OffsetCfg(
                        pos=(0.09193, -0.0016, 0.0),  # Offset from link5 to end_effector_link from URDF
                        rot=(1.0, 0.0, 0.0, 0.0)  # Quaternion (w, x, y, z)
                    )
                ),
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/omx_f/link5",
                    name="jaw",
                    offset=OffsetCfg(
                        pos=(0.09193, -0.0016, 0.0),  # Same as gripper for OMX robot
                        rot=(1.0, 0.0, 0.0, 0.0)
                    )
                ),
            ]
        )

        # Override front camera to attach to link0
        self.scene.front = TiledCameraCfg(
            prim_path="{ENV_REGEX_NS}/Robot/omx_f/link0/front_camera",
            offset=TiledCameraCfg.OffsetCfg(pos=(0.0, -0.5, 0.6), rot=(0.1650476, -0.9862856, 0.0, 0.0), convention="ros"),
            data_types=["rgb"],
            spawn=sim_utils.PinholeCameraCfg(
                focal_length=28.7,
                focus_distance=400.0,
                horizontal_aperture=38.11,
                clipping_range=(0.01, 50.0),
                lock_camera=True
            ),
            width=640,
            height=480,
            update_period=1 / 30.0,
        )

        # Remove wrist camera (OMX robot doesn't have a wrist camera mount)
        # We set it to None and will remove the observation term
        self.scene.wrist = None
        
        # Remove wrist observation from policy observations
        if hasattr(self.observations.policy, 'wrist'):
            delattr(self.observations.policy, 'wrist')



        # Update subtask config key
        if "so101_follower" in self.subtask_configs:
            self.subtask_configs["omx_robot"] = self.subtask_configs.pop("so101_follower")
