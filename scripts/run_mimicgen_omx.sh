#!/bin/bash

# Define variables
INPUT_DATASET="./datasets/mimic-lift-cube-example.hdf5"
PROCESSED_DATASET="./datasets/processed_mimic-lift-cube-omx.hdf5"
ANNOTATED_DATASET="./datasets/annotated_mimic-lift-cube-omx.hdf5"
GENERATED_DATASET="./datasets/generated_mimic-lift-cube-omx.hdf5"
FINAL_DATASET="./datasets/final_generated_mimic-lift-cube-omx.hdf5"

TASK_NAME="LeIsaac-OMX-PickOrange-Mimic-v0"

echo "Step 1: Convert joint-position-based action data to IK-based action data"
python scripts/mimic/eef_action_process.py \
    --input_file $INPUT_DATASET \
    --output_file $PROCESSED_DATASET \
    --to_ik --headless

echo "Step 2: Annotate demonstrations"
python scripts/mimic/annotate_demos.py \
    --device cuda \
    --task $TASK_NAME \
    --input_file $PROCESSED_DATASET \
    --output_file $ANNOTATED_DATASET \
    --task_type mimic_omx_keyboard \
    --enable_cameras

echo "Step 3: Generate dataset"
python scripts/mimic/generate_dataset.py \
    --device cuda \
    --num_envs 1 \
    --generation_num_trials 10 \
    --input_file $ANNOTATED_DATASET \
    --output_file $GENERATED_DATASET \
    --task_type mimic_omx_keyboard \
    --enable_cameras

echo "Step 4: Convert IK-based action data back to joint-position-based action data"
python scripts/mimic/eef_action_process.py \
    --input_file $GENERATED_DATASET \
    --output_file $FINAL_DATASET \
    --to_joint --headless

echo "MimicGen workflow completed for $TASK_NAME"
