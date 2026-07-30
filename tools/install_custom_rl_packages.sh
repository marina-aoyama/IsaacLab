#!/usr/bin/env bash
# Installs the custom skrl fork and the sliding task extension in editable mode.
# Runs on every container start (see docker-compose.yaml entrypoint) since both
# /workspace/skrl and /workspace/sliding are bind-mounted volumes attached at
# container runtime, not present in the image at build time.
set -e

echo "[install_custom_rl_packages] Installing skrl (editable) from /workspace/skrl..."
/isaac-sim/python.sh -m pip install -e /workspace/skrl

echo "[install_custom_rl_packages] Installing sliding (editable) from /workspace/sliding/source/sliding..."
/isaac-sim/python.sh -m pip install -e /workspace/sliding/source/sliding

echo "[install_custom_rl_packages] Done."
