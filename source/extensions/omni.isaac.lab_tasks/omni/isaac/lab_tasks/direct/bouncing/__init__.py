# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Shuffleboard bouncing environment.
"""

import gymnasium as gym

from . import agents
from .bouncing_env import BouncingEnv, BouncingEnvCfg

from . import run_env_cfg

##
# Register Gym environments.
##

gym.register(
    id="Isaac-bouncing-Direct-v0",
    entry_point="omni.isaac.lab_tasks.direct.bouncing:BouncingEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": BouncingEnvCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": agents.rsl_rl_ppo_cfg.CartpolePPORunnerCfg,
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_franka_cfg.yaml",
        "skrl_exp_cfg_entry_point": f"{agents.__name__}:skrl_ppo_preexp_cfg.yaml",
        "sb3_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
        "run_env_cfg": "/workspace/isaaclab/source/extensions/omni.isaac.lab_tasks/omni/isaac/lab_tasks/direct/bouncing/run_env_cfg/bouncing_env_cfg.yaml"
    },
)


