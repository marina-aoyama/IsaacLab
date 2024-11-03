
import tensorflow as tf
import matplotlib.pyplot as plt


### Plot with mean and std ###
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

event_files = [
    "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0",
    "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_15-38-44/events.out.tfevents.1730644736.slmc.761094.0",
    # Add more event files as needed
]

# Dictionary to hold steps and values from each file
all_steps_values = {}

for event_file in event_files:
    steps = []
    values = []
    for e in tf.compat.v1.train.summary_iterator(event_file):
        for v in e.summary.value:
            if v.tag == "EpisodeInfo / success_rate":  # Replace with your specific tag
                steps.append(e.step * 8192)  # Scale steps as needed
                values.append(v.simple_value * 100.0)  # Scale values as needed
    
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
plt.plot(all_steps, mean_values, label="Mean Success Rate")
plt.fill_between(all_steps, np.array(mean_values) - np.array(std_values), np.array(mean_values) + np.array(std_values), alpha=0.2, label="Standard Deviation")
plt.xlabel("Training Step")
plt.ylabel("Success rate (%)")
plt.title("Training Progress with Mean and Standard Deviation")
plt.legend()

# Save the plot
plt.savefig("./tensorboard_mean_std_plot.png")
plt.close()

### Plot from one file ###
# # event_file = "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_20-53-50/events.out.tfevents.1730667249.suprim.823174.0"
# event_file = "/workspace/isaaclab/logs/skrl/sliding_direct/2024-11-03_14-38-44/events.out.tfevents.1730644735.slmc.761093.0"
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

