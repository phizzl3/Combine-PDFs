"""

Load (use defaults first if not found) json data from
file, and use that data to generate a settings file for import.

"""

from pathlib import Path
from utils.loadjsondata import loadjson
from utils.resolvestrdir import resolvedir

# json file location
JSON = Path().home() / "PyAppFiles" / "Combine PDFs" / "settings.json"

# Default values for json data
DEFAULTS = {
    "target directory": "~/Downloads",
    "working folder name": "Combine_PDFs",
    "output file name": "_Merged_PDF.pdf",
}

# Load (or set defaults) settings json data
data = loadjson(JSON, default_data=DEFAULTS)

# Format data for use as Path objects
target_dir = resolvedir(data["target directory"])
working_dir = data["working folder name"]
file_name = data["output file name"]

# Formatted settings data (Import this)
SETTINGS = {
    "merge folder": target_dir / working_dir,
    "output file": target_dir / working_dir / file_name,
}
