
import tensorflow as tf
import matplotlib.pyplot as plt


### Plot with mean and std ###
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


import os

### Each trial ###
# test_case_names = ["friction_gt", "com_gt", "friccom_gt"]
# test_case_names = ["com_gt"]
# test_case_names = ["friction_dr", "friction_gt"]
test_case_names = ["com_dr", "com_gt"]
# test_case_names = ["friccom_dr", "friccom_gt"]

test_case_labels_dicr = {
    "friction_dr": "Friction (DR)", 
    "friction_gt": "Friction (DR+Groundtruth)", 
    "com_dr": "CoM (DR)", 
    "com_gt": "CoM (DR+Groundtruth)", 
    "friccom_dr": "Friction + CoM (DR)", 
    "friccom_gt": "Friction + CoM (DR+Groundtruth)", 
}

event_files_dir = {
    "friction_gt": 'source/tensorboard_plot/friction_gt',   # Adjust path if needed
    "com_gt": 'source/tensorboard_plot/com_gt',   # Adjust path if needed
    "friccom_gt": 'source/tensorboard_plot/friccom_gt',   # Adjust path if needed
    "friction_dr": 'source/tensorboard_plot/fric_dr',   # Adjust path if needed
    "com_dr": 'source/tensorboard_plot/com_dr',   # Adjust path if needed
    "friccom_dr": 'source/tensorboard_plot/friccom_dr',   # Adjust path if needed
}

# base_dir = 'source/tensorboard_plot/friction_gt'  # Adjust path if needed

event_files_dict = {}

for test_case_name in test_case_names: 
    event_files = []
    # Iterate through each directory within 'friction_dt'
    for root, dirs, files in os.walk(event_files_dir[test_case_name]):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            # List all files in the subdirectory and check for event files
            for file_name in os.listdir(dir_path):
                if file_name.startswith("events.out.tfevents"):
                    event_file_path = os.path.join(dir_path, file_name)
                    print(f"Found event file: {event_file_path}")
                    event_files.append(event_file_path)
    event_files_dict[test_case_name] = event_files

print(event_files_dict)

# event_files = [
#     "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0",
#     "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_15-38-44/events.out.tfevents.1730644736.slmc.761094.0",
#     # Add more event files as needed
# ]

### Code starts here ###
# plt.figure(figsize=(12, 6))  # Width: 12 inches, Height: 6 inches
# for test_case_name in test_case_names: 
#     # Dictionary to hold steps and values from each file
#     all_steps_values = {}
#     all_steps_values = {}

#     for event_file in event_files_dict[test_case_name]:
#         print("Event file:", event_file)
#         steps = []
#         values = []
        
#         # Extract steps and values from each event file
#         for e in tf.compat.v1.train.summary_iterator(event_file):
#             for v in e.summary.value:
#                 if v.tag == "EpisodeInfo / success_rate":  # Replace with your specific tag
#                     steps.append(e.step * 8192)  # Scale steps as needed
#                     values.append(v.simple_value * 100.0)  # Scale values as needed

#         # Store steps and values for this file
#         all_steps_values[event_file] = (steps, values)

#         # Plot each line individually
#         plt.plot(steps, values, label=f"Run {event_file}")

#     # for event_file in event_files_dict[test_case_name]:
#     #     print("Event fileeeee")
#     #     print(event_file)
#     #     steps = []
#     #     values = []
#     #     for e in tf.compat.v1.train.summary_iterator(event_file):
#     #         for v in e.summary.value:
#     #             if v.tag == "EpisodeInfo / success_rate":  # Replace with your specific tag
#     #                 steps.append(e.step * 8192)  # Scale steps as needed
#     #                 values.append(v.simple_value * 100.0)  # Scale values as neede
#     #                 # print(steps)
#     #                 # print(values)
        
#     #     # Store steps and values for this file
#     #     all_steps_values[event_file] = (steps, values)

#     # # Align steps and calculate mean and std dev
#     # all_steps = sorted(set(step for steps, _ in all_steps_values.values() for step in steps))
#     # mean_values = []
#     # std_values = []

#     # for step in all_steps:
#     #     step_values = [values[steps.index(step)] for steps, values in all_steps_values.values() if step in steps]
#     #     mean_values.append(np.mean(step_values))
#     #     std_values.append(np.std(step_values))

#     # # Plot mean with standard deviation as shaded area
#     # plt.plot(all_steps, mean_values, label="Mean Success Rate")
#     # plt.fill_between(all_steps, np.array(mean_values) - np.array(std_values), np.array(mean_values) + np.array(std_values), alpha=0.2, label="Standard Deviation")

# plt.xlabel("Training Step")
# plt.ylabel("Success rate (%)")
# # plt.title("Training Progress with Mean and Standard Deviation")
# # plt.legend()
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# plt.tight_layout()  # Adjust layout to fit everything in the window

# # Save the plot
# plt.savefig("./tensorboard_mean_std_plot.png")
# plt.close()
# ### Code ends here ###

# ### Mean and std ###
# test_case_names = ["friction_gt", "com_gt", "friccom_gt"]
# # test_case_names = ["friccom_gt"]

# event_files_dir = {
#     "friction_gt": 'source/tensorboard_plot/friction_gt',   # Adjust path if needed
#     "com_gt": 'source/tensorboard_plot/com_gt',   # Adjust path if needed
#     "friccom_gt": 'source/tensorboard_plot/friccom_gt',   # Adjust path if needed
# }

# # base_dir = 'source/tensorboard_plot/friction_gt'  # Adjust path if needed

# event_files_dict = {}

# for test_case_name in test_case_names: 
#     event_files = []
#     # Iterate through each directory within 'friction_dt'
#     for root, dirs, files in os.walk(event_files_dir[test_case_name]):
#         for dir_name in dirs:
#             dir_path = os.path.join(root, dir_name)
            
#             # List all files in the subdirectory and check for event files
#             for file_name in os.listdir(dir_path):
#                 if file_name.startswith("events.out.tfevents"):
#                     event_file_path = os.path.join(dir_path, file_name)
#                     print(f"Found event file: {event_file_path}")
#                     event_files.append(event_file_path)
#     event_files_dict[test_case_name] = event_files

# print(event_files_dict)

# # event_files = [
# #     "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0",
# #     "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_15-38-44/events.out.tfevents.1730644736.slmc.761094.0",
# #     # Add more event files as needed
# # ]

###  Code starts here ###
plt.figure(figsize=(12, 6))  # Width: 12 inches, Height: 6 inches
for test_case_name in test_case_names: 
    # Dictionary to hold steps and values from each file
    all_steps_values = {}

    for event_file in event_files_dict[test_case_name]:
        print("Event fileeeee")
        print(event_file)
        steps = []
        values = []
        for e in tf.compat.v1.train.summary_iterator(event_file):
            for v in e.summary.value:
                if v.tag == "EpisodeInfo / success_rate":  # Replace with your specific tag
                    steps.append(e.step * 8192)  # Scale steps as needed
                    values.append(v.simple_value * 100.0)  # Scale values as neede
                    # print(steps)
                    # print(values)
        
        # Store steps and values for this file
        all_steps_values[event_file] = (steps, values)

    # Align steps and calculate mean and std dev
    all_steps = sorted(set(step for steps, _ in all_steps_values.values() for step in steps))
    mean_values = []
    std_values = []

    for step in all_steps:
        step_values = [values[steps.index(step)] for steps, values in all_steps_values.values() if step in steps]
        mean_values.append(np.mean(step_values))
        std_values.append(np.std(step_values))

    # Plot mean with standard deviation as shaded area
    # plt.plot(all_steps, mean_values, label="Mean Success Rate")
    plt.plot(all_steps, mean_values, label=test_case_labels_dicr[test_case_name])
    # plt.fill_between(all_steps, np.array(mean_values) - np.array(std_values), np.array(mean_values) + np.array(std_values), alpha=0.2, label="Standard Deviation")
    plt.fill_between(all_steps, np.array(mean_values) - np.array(std_values), np.array(mean_values) + np.array(std_values), alpha=0.2)

plt.xlabel("Training Step")
plt.ylabel("Success rate (%)")
# plt.title("Training Progress with Mean and Standard Deviation")
# plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()  # Adjust layout to fit everything in the window

# Save the plot
plt.savefig("./tensorboard_mean_std_plot.png")
plt.close()
### Code ends here ###


# ## Plot from one file ###
# # event_file = "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_20-53-50/events.out.tfevents.1730667249.suprim.823174.0"
# # event_file = "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0"
# event_file = "/workspace/isaaclab/source/tensorboard_plot/friction_gt/2024-11-03_16-24-59/events.out.tfevents.1730651119.suprim.652949.0"
# steps = []
# values = []

# for e in tf.compat.v1.train.summary_iterator(event_file):
#     for v in e.summary.value:
#         # if v.tag == "Reward / Total reward (mean)":  # Replace with the specific tag you want to plot
#         if v.tag == "EpisodeInfo / success_rate":  # Replace with the specific tag you want to plot
#             steps.append(e.step)
#             values.append(v.simple_value)

# steps = [x * 8192 for x in steps]
# values = [x * 100.0 for x in values]

# # Plot the data
# plt.plot(steps, values)
# plt.xlabel("Training Step")
# plt.ylabel("Success rate (%)")
# plt.title("Training Progress")
# # plt.show()
# plt.savefig("./tensorboard_plot.png")  # Saves as "plot.png" in the current directory
# plt.close()  # Close the figure if you don’t need to display it with plt.show()

### Check tags ###
# event_file = "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0"
# tags = set()  # Use a set to store unique tags

# # Iterate through the event file and collect tags
# for e in tf.compat.v1.train.summary_iterator(event_file):
#     for v in e.summary.value:
#         tags.add(v.tag)

# # Print all unique tags
# print("Tags found in the event file:")
# for tag in tags:
#     print(tag)

