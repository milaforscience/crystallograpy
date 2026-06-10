from .utils import get_wyckoff_index, load_database

# Load space group and Wyckoff data when the package is imported
spacegroups = load_database("spacegroups.yaml")
wyckoff = load_database("wyckoff.yaml")

# Make configurations available at package level
__all__ = ["spacegroups", "wyckoff", "get_wyckoff_index"]
