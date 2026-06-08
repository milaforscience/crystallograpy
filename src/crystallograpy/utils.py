from pathlib import Path

import yaml

# Path to the yaml directory relative to this __init__.py file
YAML_DIR = Path(__file__).parent.parent.parent / "yaml"

# Dictionary to store databases
_databases = {"wyckoff.yaml": {}, "spacegroups.yaml": {}}


def load_database(filename: str) -> dict:
    """Load YAML database into memory."""
    global _databases

    # Do not reload if already loaded
    if _databases[filename]:
        return _databases[filename]

    # Load YAML file
    try:
        with open(YAML_DIR / filename, "r") as f:
            _databases[filename] = yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: could not load {filename}: {e}")

    return _databases[filename]
