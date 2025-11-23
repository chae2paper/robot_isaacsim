from isaaclab.envs.mimic_env_cfg import MimicEnvCfg
from isaaclab.utils import configclass

from .lift_cube_mimic_env_cfg import LiftCubeMimicEnvCfg
from leisaac.assets.robots.omx_robot import OMX_ROBOT_CFG


@configclass
class LiftCubeOMXMimicEnvCfg(LiftCubeMimicEnvCfg):
    """
    Configuration for the lift cube task with mimic environment using OMX robot.
    """

    def __post_init__(self):
        super().__post_init__()
        
        # Override robot
        self.scene.robot = OMX_ROBOT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        
        # Update datagen config name if needed, but keeping it similar for now
        self.datagen_config.name = "lift_cube_omx_task_v0"
