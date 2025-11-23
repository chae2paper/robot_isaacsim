#!/bin/bash

# Define variables
TASK_NAME="LeIsaac-OMX-PickOrange-v0"
DATASET_FILE="./datasets/mimic-lift-cube-example.hdf5"

echo "Running Dataset Replay for $TASK_NAME"
python scripts/environments/teleoperation/replay.py \
    --task=$TASK_NAME \
    --num_envs=1 \
    --device=cuda \
    --enable_cameras \
    --replay_mode=action \
    --dataset_file=$DATASET_FILE \
    --task_type=omx_keyboard
