

#!/bin/bash

num_runs=1  # Set the number of runs

# Function to run a simulation
run_simulation() {
    local task_name=$1
    local output_file=$2
    echo "Running simulation $task_name..."
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    seed=$(( (RANDOM << 16) + RANDOM ))
    
    # Run the command and redirect output
    ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task "$task_name" --headless --seed "$seed" > "$output_file" 2>&1
    local status=$?
    
    echo "Ensuring all processes are terminated..."
    pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
    if [ $status -ne 0 ]; then
        echo "Simulation $task_name failed. Output saved to $output_file"
    else
        echo "Simulation $task_name complete. Output saved to $output_file"
    fi
    
    sleep 5  # Shorter wait period if using pkill
}

# Fric DR
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v8" "$(dirname "$0")/logs/bash_output/output_run_fric_dr_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done

# Fric GT
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v9" "$(dirname "$0")/logs/bash_output/output_run_fric_gt_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done

# CoM DR
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v10" "$(dirname "$0")/logs/bash_output/output_run_com_dr_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done

# CoM GT
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v11" "$(dirname "$0")/logs/bash_output/output_run_com_gt_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done

# Fric + CoM DR
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v12" "$(dirname "$0")/logs/bash_output/output_run_friccom_dr_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done

# Fric + CoM GT
for ((i=1; i<=num_runs; i++))
do
    run_simulation "Isaac-Sliding-Direct-v13" "$(dirname "$0")/logs/bash_output/output_run_friccom_gt_$(date +"%Y-%m-%d_%H-%M-%S")_$i.txt"
done





# #!/bin/bash


# num_runs=1  # Set the number of runs

# # Fric DR
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v8 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_fric_dr_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

# # Fric GT
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v9 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_fric_gt_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

# # CoM DR
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v10 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_com_dr_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

# # CoM GT
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v11 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_com_gt_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

# # Fric + CoM DR
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v12 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_friccom_dr_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done

# # Fric + CoM GT
# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v13 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_friccom_gt_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done




# # General
# num_runs=2  # Set the number of runs

# for ((i=1; i<=num_runs; i++))
# do
#     echo "Running simulation $i..."
#     timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
#     seed=$(( (RANDOM << 16) + RANDOM ))
#     ./isaaclab.sh -p source/standalone/workflows/skrl/train_feedback.py --task Isaac-Sliding-Direct-v7 --headless --seed "$seed" > "$(dirname "$0")/logs/bash_output/output_run_${timestamp}_$i.txt" 2>&1
 
#     echo "Ensuring all processes are terminated..."
#     pkill -f "isaaclab.sh"  # Adjust this if needed for specific processes
    
#     echo "Simulation $i complete. Output saved to output_run_${timestamp}_$i.txt"
#     sleep 5  # Shorter wait period if using pkill
# done


