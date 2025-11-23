from isaaclab.utils import configclass

from .lift_cube_env_cfg import LiftCubeEnvCfg
from leisaac.assets.robots.omx_robot import OMX_ROBOT_CFG


@configclass
class LiftCubeOMXEnvCfg(LiftCubeEnvCfg):
    """
    Configuration for the lift cube task with OMX robot.
    """

    def __post_init__(self):
        super().__post_init__()
        
        # Override robot
        self.scene.robot = OMX_ROBOT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
