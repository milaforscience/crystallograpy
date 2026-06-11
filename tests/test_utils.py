import pytest

from crystallograpy import get_wyckoff_index


@pytest.mark.parametrize(
    "spacegroup, letter, wyckoff_index",
    [
        (1, "a", 1),
        (2, "a", 2),
        (2, "b", 3),
        (2, "c", 4),
        (2, "d", 5),
        (2, "e", 6),
        (2, "f", 7),
        (2, "g", 8),
        (2, "h", 9),
        (2, "i", 10),
        (3, "a", 11),
        (3, "b", 12),
        (3, "c", 13),
        (3, "d", 14),
        (3, "e", 15),
        (4, "a", 16),
        (10, "a", 2),
        (10, "b", 4),
        (10, "c", 3),
        (10, "d", 5),
        (10, "e", 6),
        (10, "f", 8),
        (10, "g", 7),
        (10, "h", 9),
        (10, "i", 27),
        (10, "j", 28),
        (10, "k", 29),
        (10, "l", 30),
        (10, "m", 31),
        (10, "n", 32),
        (10, "o", 33),
        (47, "a", 2),
        (47, "b", 5),
        (47, "x", 202),
        (47, "y", 203),
        (47, "z", 204),
        (47, "α", 198),
        (47, "alpha", 198),
    ],
)
def test__get_wyckoff_index__returns_expected_index_from_pair(
    spacegroup, letter, wyckoff_index
):
    assert get_wyckoff_index(spacegroup, letter) == wyckoff_index


@pytest.mark.parametrize(
    "name, wyckoff_index",
    [
        ("1a", 1),
        ("2a", 2),
        ("2b", 3),
        ("2c", 4),
        ("2d", 5),
        ("2e", 6),
        ("2f", 7),
        ("2g", 8),
        ("2h", 9),
        ("2i", 10),
        ("3a", 11),
        ("3b", 12),
        ("3c", 13),
        ("3d", 14),
        ("3e", 15),
        ("4a", 16),
        ("10a", 2),
        ("10b", 4),
        ("10c", 3),
        ("10d", 5),
        ("10e", 6),
        ("10f", 8),
        ("10g", 7),
        ("10h", 9),
        ("10i", 27),
        ("10j", 28),
        ("10k", 29),
        ("10l", 30),
        ("10m", 31),
        ("10n", 32),
        ("10o", 33),
        ("47a", 2),
        ("47b", 5),
        ("47x", 202),
        ("47y", 203),
        ("47z", 204),
        ("47α", 198),
        ("47alpha", 198),
    ],
)
def test__get_wyckoff_index__returns_expected_index_from_pair(name, wyckoff_index):
    assert get_wyckoff_index(name=name) == wyckoff_index


@pytest.mark.parametrize(
    "spacegroup, letter",
    [
        (1, "b"),
        (1, "c"),
        (2, "j"),
        (2, "k"),
        (3, "f"),
        (3, "g"),
        (230, "i"),
    ],
)
def test__get_wyckoff_index__invalid_space_group_and_letter_pair_returns_none(
    spacegroup, letter
):
    with pytest.warns(
        UserWarning, match="does not correspond to a valid Wyckoff position"
    ):
        assert get_wyckoff_index(spacegroup, letter) is None


@pytest.mark.parametrize(
    "spacegroup, letter",
    [
        (0, "a"),
        (-2, "a"),
        (231, "b"),
    ],
)
def test__get_wyckoff_index__incorrect_spacegroup_returns_none(spacegroup, letter):
    with pytest.warns(
        UserWarning, match="The space group number must be between 1 and 230"
    ):
        assert get_wyckoff_index(spacegroup, letter) is None


@pytest.mark.parametrize(
    "spacegroup, letter",
    [
        (2, "aaaa"),
        (2, "ab"),
        (2, "a "),
        (2, "æ"),
        (2, "@"),
        (2, "?"),
    ],
)
def test__get_wyckoff_index__incorrect_spacegroup_returns_none(spacegroup, letter):
    with pytest.warns(UserWarning, match="The letter must be a, b, c, ..."):
        assert get_wyckoff_index(spacegroup, letter) is None


@pytest.mark.parametrize(
    "spacegroup",
    [
        (1),
        (2),
        (3),
        (4),
        (10),
        (230),
    ],
)
def test__get_wyckoff_index__missing_letter_returns_none(spacegroup):
    with pytest.warns(UserWarning, match="the parameter letter is None"):
        assert get_wyckoff_index(spacegroup=spacegroup) is None


@pytest.mark.parametrize(
    "letter",
    [
        ("a"),
        ("b"),
        ("j"),
        ("k"),
        ("l"),
        ("z"),
    ],
)
def test__get_wyckoff_index__missing_spacegroup_returns_none(letter):
    with pytest.warns(UserWarning, match="the parameter spacegroup is None"):
        assert get_wyckoff_index(letter=letter) is None


@pytest.mark.parametrize(
    "name",
    [
        ("2aa"),
        ("b"),
        ("1 j"),
        ("b2"),
        ("2"),
        ("2b2"),
    ],
)
def test__get_wyckoff_index__incorrect_name_returns_none(name):
    with pytest.warns(
        UserWarning,
        match="the space group and the letter could not be successfully retrieved",
    ):
        assert get_wyckoff_index(name=name) is None
