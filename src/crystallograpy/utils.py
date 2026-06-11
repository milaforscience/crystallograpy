import re
import warnings
from pathlib import Path

import yaml

# Path to the yaml directory relative to this __init__.py file
YAML_DIR = Path(__file__).parent.parent.parent / "yaml"

# Dictionary to convert letters to indices
LETTER2INDEX = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "α": 26,
}

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
    if name is not None:
        match = re.match(r"^(\d+)([a-zA-Z])$", name)
        if match:
            spacegroup_name, letter_name = int(match.group(1)), match.group(2)
        # Catch special case of Wyckoff position 47α
        elif name == "47α" or name == "47alpha":
            spacegroup_name, letter_name = 47, "α"
        else:
            warnings.warn(
                f"A Wyckoff name was provided ({name}) but the space group and the "
                "letter could not be successfully retrieved. The format should be an "
                "integer followed by a letter, such as 1a, 2i, 82f, 225k, etc."
            )
            return None
        if spacegroup is not None and spacegroup != spacegroup_name:
            warnings.warn(
                f"A spacegroup parameter ({spacegroup}) and a name parameter "
                f"({name}) have been provided by they do not coincide. None will be "
                "returned."
            )
            return None
        if letter is not None and letter != letter_name:
            warnings.warn(
                f"A letter parameter ({letter}) and a name parameter ({name}) "
                "have been provided by they do not coincide. None will be returned."
            )
            return None
        spacegroup = spacegroup_name
        letter = letter_name

    if spacegroup is not None:
        if letter is None:
            warnings.warn(
                f"A space group number ({spacegroup}) was provided but the parameter "
                "letter is None."
            )
            return None
        if spacegroup < 1 or spacegroup > 230:
            warnings.warn(
                f"The space group number must be between 1 and 230. {spacegroup} was "
                "received, which is invalid."
            )
            return None
        # Catch special case of Wyckoff position 47α, where 'alpha' as the letter is
        # accepted
        if letter == "alpha":
            letter = "α"
        if letter not in LETTER2INDEX:
            warnings.warn(
                f"The letter must be a, b, c, ..., z, α. {letter} was "
                "received, which is invalid."
            )
            return None
    else:
        if letter is not None:
            warnings.warn(
                f"A Wyckoff letter ({letter}) was provided but the parameter "
                "spacegroup is None."
            )
            return None

    letter_index = LETTER2INDEX[letter]

    spacegroups = load_database("spacegroups.yaml")
    spacegroup_data = spacegroups[spacegroup]
    wyckoff_indices = spacegroup_data["wyckoff_positions"]
    if (letter_index + 1) > len(wyckoff_indices):
        warnings.warn(
            f"The space group and letter pair ({spacegroup}, {letter}) does not "
            "correspond to a valid Wyckoff position."
        )
        return None
    wyckoff_index = wyckoff_indices[::-1][letter_index]
    return wyckoff_index
