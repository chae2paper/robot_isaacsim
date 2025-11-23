#!/bin/bash

# Define variables
TASK_NAME="LeIsaac-OMX-PickOrange-v0"
DATASET_FILE="./datasets/mimic-lift-cube-example.hdf5"

echo "Running Teleoperation for $TASK_NAME"
python scripts/environments/teleoperation/teleop_se3_agent.py \
    --task=$TASK_NAME \
    --teleop_device=omx_keyboard \
    --num_envs=1 \
    --device=cuda \
    --enable_cameras \
    --record \
    --dataset_file=$DATASET_FILE
