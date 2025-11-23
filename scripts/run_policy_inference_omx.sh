#!/bin/bash

# Define variables
TASK_NAME="LeIsaac-OMX-PickOrange-v0"

echo "Running Policy Inference for $TASK_NAME"
python scripts/evaluation/policy_inference.py \
    --task=$TASK_NAME \
    --eval_rounds=10 \
    --policy_type=gr00tn1.5 \
    --policy_host=localhost \
    --policy_port=5555 \
    --policy_timeout_ms=5000 \
    --policy_action_horizon=16 \
    --policy_language_instruction="Pick up the orange and place it on the plate" \
    --device=cuda \
    --enable_cameras
