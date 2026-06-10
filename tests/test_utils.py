import pytest

from crystallograpy import get_wyckoff_index


@pytest.mark.parametrize(
    "spacegroup, letter, wyckoff_index",
    [
        (1, "a", 1),
    ],
)
def test__get_wyckoff_index__returns_expected_index_from_pair(
    spacegroup, letter, wyckoff_index
):
    assert get_wyckoff_index(spacegroup, letter) == wyckoff_index
