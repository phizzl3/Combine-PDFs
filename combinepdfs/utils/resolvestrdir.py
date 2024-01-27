"""

Gets a string formatted directory and returns
a resolved pathlib.Path object. Resolves "~/" to
user's home folder.
    
"""

__version__ = "1.0.0"

from pathlib import Path


def resolvedir(dirstr: str) -> Path:
    """Gets a string formatted directory and returns
    a resolved pathlib.Path object. Resolves "~/" to
    user's home folder.

    Args:
        dirstr (str): String formatted directory.

    Returns:
        Path: pathlib.Path object of resoved directory.
    """
    # Replace with home folder.
    if dirstr[0:2] == "~/":
        filepath = Path().home() / dirstr[2:]
        return filepath.resolve()
    # Resolve and return
    return Path(dirstr).resolve()
