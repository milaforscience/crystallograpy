import re
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


def get_wyckoff_index(
    spacegroup: int | None = None,
    letter: str | None = None,
    name: str | None = None,
) -> int:
    """Return the Wyckoff index corresponding to a pair of space group number and
    Wyckoff letter.

    Parameters
    ----------
    spacegroup : int or None, optional
        An integer between 1 and 230 corresponding to one of the international numbers
        identifying a space group. If ``None``, the Wyckoff position must be identified
        through the parameter ``name``. If not None, ``letter`` must also be specified.
    letter : str or None, optional
        A string containing a single character identifying the Wyckoff position of a
        space group as in the International Tables for Crystallography. If ``None``,
        the Wyckoff position must be identified through the parameter ``name``.
        If not None, ``spacegroup`` must also be specified.
    name : str or None, optional
        A string containing both an integer between 1 and 230 identifying the
        international number of a space group, followed by a letter identifying a
        specific Wyckoff position. If ``None``, the Wyckoff position must be identified
        through the parameters ``spacegroup`` and ``letter`` separately.

    Returns
    -------
    index : int or None, optional
        An integer between 1 and 990 corresponding to a unique identifier of a
        Wyckoff position, as per the data stored in ``yaml/wyckoff.yaml``.
    """
    if spacegroup is not None:
        if letter is None:
            raise ValueError(
                f"A space group number ({spacegroup}) was provided but the parameter "
                "letter is None."
            )
        if spacegroup < 1 or spacegroup > 230:
            raise ValueError(
                f"The space group number must be between 1 and 230. {spacegroup} was "
                "received, which is invalid."
            )
    else:
        if letter is not None:
            raise ValueError(
                f"A Wyckoff letter ({letter}) was provided but the parameter "
                "spacegroup is None."
            )
    if name is not None:
        match = re.match(r"^(\d+)([a-zA-Z])$", name)
        if match:
            spacegroup_name, letter_name = int(match.group(1)), match.group(2)
        else:
            raise ValueError(
                f"A Wyckoff name was provided ({name}) but the space group and the "
                "letter could not be successfully retrieved. The format should be an "
                "integer followed by a letter, such as 1a, 2i, 82f, 225k, etc."
            )
