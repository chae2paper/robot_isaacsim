from pathlib import Path

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from leisaac.utils.constant import ASSETS_ROOT


"""Configuration for the OMX Robot."""
OMX_ROBOT_ASSET_PATH = Path(ASSETS_ROOT) / "robots" / "omx_robot.usd"

OMX_ROBOT_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(OMX_ROBOT_ASSET_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=4,
            fix_root_link=True,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        # pos=(2.2, -0.61, 0.89),
        # rot=(0.0, 0.0, 0.0, 1.0),
        pos=(2.2, -0.61, 0.92),
        rot=(0.0, 0.0, 0.0, 1.0),
        joint_pos={
            "joint1": 0.0,
            "joint2": 0.0,
            "joint3": 0.0,
            "joint4": 0.0,
            "joint5": 0.0,
            "gripper_joint_1": 0.0
        }
    ),
    actuators={
        "sts3215-gripper": ImplicitActuatorCfg(
            joint_names_expr=["gripper_joint_1"],
            effort_limit_sim=10,
            velocity_limit_sim=10,
            stiffness=17.8,
            damping=0.60,
        ),
        "sts3215-arm": ImplicitActuatorCfg(
            joint_names_expr=["joint[1-5]"],
            effort_limit_sim=10,
            velocity_limit_sim=10,
            stiffness=17.8,
            damping=0.60,
        )
    },
    soft_joint_pos_limit_factor=1.0,
)

# joint limit written in USD (degree)
OMX_ROBOT_USD_JOINT_LIMITS = {
    "joint1": (-360.0, 360.0),
    "joint2": (-360.0, 360.0),
    "joint3": (-360.0, 360.0),
    "joint4": (-360.0, 360.0),
    "joint5": (-360.0, 360.0),
    "gripper_joint_1": (-360.0, 360.0),
}

OMX_ROBOT_REST_POSE_RANGE = {
    "joint1": (-30.0, 30.0),
    "joint2": (-30.0, 30.0),
    "joint3": (-30.0, 30.0),
    "joint4": (-30.0, 30.0),
    "joint5": (-30.0, 30.0),
    "gripper_joint_1": (-30.0, 30.0),
}
