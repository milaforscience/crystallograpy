import os
from pathlib import Path

import yaml

# Path to the yaml directory relative to this __init__.py file
YAML_DIR = Path(__file__).parent.parent.parent / "yaml"

# Dictionary to store Wyckoff positions data
_wyckoff = {}


def load_wyckoff():
    """Load yaml/wyckoff.yaml into memory."""
    global _wyckoff

    # Do not reload if already loaded
    if _wyckoff:
        return _wyckoff

    # Load wyckoff.yaml
    try:
        with open(YAML_DIR / "wyckoff.yaml", "r") as f:
            _wyckoff = yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: could not load wyckoff.yaml: {e}")

    return _wyckoff


# Load Wyckoff data when the package is imported
wyckoff = load_wyckoff()

# Make configurations available at package level
__all__ = ["wyckoff"]
