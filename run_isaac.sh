
#!/bin/bash

num_runs=2  # Set the number of runs

for ((i=1; i<=num_runs; i++))
do
    echo "Running simulation $i..."
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    seed=$(( (RANDOM << 16) + RANDOM ))
    # ./isaaclab.sh -p source/standalone/workflows/skrl/play2_feedback.py --task Isaac-Sliding-Direct-v7 --num_envs 32
    # ./isaaclab.sh -p source/standalone/workflows/skrl/play2_feedback.py --task Isaac-Sliding-Direct-v7 --headless > "output_run_$i.txt" 2>&1
    # ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v7 --headless > "$(dirname "$0")/logs/bash_output/output_run_$i.txt" 2>&1
    # ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v7 --headless > "$(dirname "$0")/logs/bash_output/output_run_${timestamp}_$i.txt" 2>&1
    ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v7 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_${timestamp}_$i.txt" 2>&1
 
    echo "Ensuring all processes are terminated..."
    pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
    echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
    sleep 5  # Shorter wait period if using pkill
done




# #!/bin/bash
 
# num_runs=5  # Set the number of runs
 
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     ./isaaclab.sh -p source/standalone/workflows/skrl/play2_feedback.py --task Isaac-Sliding-Direct-v7 --headless > "output_run_$i.txt" 2>&1
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
#     echo "Simulation $i complete. Output saved to output_run_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

