# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Shuffleboard sliding environment.
"""

import gymnasium as gym

from . import agents
from .sliding_pandagym_prop_env import SlidingExample2Env, SlidingExample2EnvCfg

from . import run_env_cfg

##
# Register Gym environments.
##

gym.register(
    id="Isaac-SlidingExample2-Direct-v0",
    entry_point="omni.isaac.lab_tasks.direct.sliding_example2:SlidingExample2Env",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": SlidingExample2EnvCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": agents.rsl_rl_ppo_cfg.CartpolePPORunnerCfg,
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
        "skrl_exp_cfg_entry_point": f"{agents.__name__}:skrl_ppo_preexp_cfg.yaml",
        "sb3_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
        "run_env_cfg": "/workspace/isaaclab/source/extensions/omni.isaac.lab_tasks/omni/isaac/lab_tasks/direct/sliding_example2/run_env_cfg/sliding_env_cfg.yaml"
    },
)

