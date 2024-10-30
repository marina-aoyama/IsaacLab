#!/bin/bash

num_runs=5  # Set the number of runs

for ((i=1; i<=num_runs; i++))
do
    echo "Running simulation $i..."
    ./isaaclab.sh -p source/standalone/workflows/skrl/play2_feedback.py --task Isaac-Sliding-Direct-v7 --num_envs 32
 
    echo "Ensuring all processes are terminated..."
    pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
    echo "Simulation $i complete. Output saved to output_run_$i.txt"
    sleep 5  # Shorter wait period if using pkill
done
