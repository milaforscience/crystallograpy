from cyrstallograpy import spacegroups


class SpaceGroup:
    """Class to represent space groups.

    An instance of this SpaceGroup class is meant to represent one of the 230 space
    groups as stored in ``yaml/spacegroups.yaml``.

    A space group is identified by an integer corresponding to the international
    number, as per the International Tables for Crystallography.
    """

    def __init__(self, number: int):
        """Initialize a SpaceGroup instance.

        Parameters
        ----------
        number : int
            An integer between 1 and 230 corresponding to an international number, as
            per the data stored in ``yaml/spacegroup.yaml`` and the International
            Tables for Crystallography.
        """
        # Read space group by its number
        assert number >= 1 and number <= 230
        data = spacegroups[index]

        self.symbol = data.symbol
        self.full_symbol = data.full_symbol
        self.crystal_system = data.crystal_system
        self.crystal_lattice = data.crystal_lattice
        self.crystal_lattice_system_index = data.crystal_lattice_system_index
        self.point_symmetry = data.point_symmetry
        self.point_symmetry_idx = data.point_symmetry_idx
        self.point_group = data.point_group
        self.crystal_class = data.crystal_class
