from cyrstallograpy import wyckoff


class Wyckoff:
    """Class to represent a unique Wyckoff position.

    An instance of this Wyckoff class is meant to represent one of the Wyckoff
    positions stored in ``yaml/wyckoff.yaml``.

    For example, the Wyckoff position with index 1 corresponds to the Wyckoff position
    a in space group 1, which is unique to space group 1 and corresponds to coordinates
    (x, y z). However, the Wyckoff position in with index 2 can be found in space group
    2 by the letter a, in space group 10 by the letter a, and in a number of other
    space groups. It corresponds to coordinates (0, 0, 0).

    A Wyckoff position can be identified in the following three ways:
    - By its unique index as stored in ``yaml/wyckoff.yaml``, for example, 2.
    - By a tuple of space group number and letter, as indicated in the International
      Tables for Crystallography, for example, (2, a) or (10, a).
    - By a string name containing the space group number and the letter, for example
      ``"2a"`` or ``"10a"``.
    """

    def __init__(
        self,
        index: int | None = None,
        spacegroup: int | None = None,
        letter: str | None = None,
        name: str | None = None,
    ):
        """Initialize a Wyckoff instance.

        Parameters
        ----------
        index : int or None, optional
            An integer between 1 and 990 corresponding to a unique identifier of a
            Wyckoff position, as per the data stored in ``yaml/wyckoff.yaml``. If
            ``None``, the Wyckoff position must be identified through other parameters.
        spacegroup : int or None, optional
            An integer between 1 and 230 corresponding to one of the international
            numbers identifying a space group. If ``None``, the Wyckoff position must
            be identified through other parameters. If not None, ``letter`` must also
            be specified.
        letter : str or None, optional
            A string containing a single character identifying the Wyckoff position of
            a space group as in the International Tables for Crystallograpy. If
            ``None``, the Wyckoff position must be identified through other parameters.
            If not None, ``spacegroup`` must also be specified.
        name : str or None, optional
            A string containing both an integer between 1 and 230 identifying the
            international number of a space group, followed by a letter identifying a
            specific Wyckoff position. If ``None``, the Wyckoff position must be
            identified through other parameters.
        """
        # Read Wyckoff position by index
        if index:
            assert index >= 1 and index <= 990
            data = wyckoff[index]

        self.name = data.name
        self.multiplicity = data.multiplicity
        self.is_special = data.is_special
        self.is_fixed = data.is_fixed
        self.spacegroups = data.spacegroups
        self.offset = data.offset
        self.algebraic = data.algebraic
        self.positions = data.positions
