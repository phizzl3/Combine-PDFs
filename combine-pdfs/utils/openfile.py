"""
Open a specified (passed) file in it's default application
based on detected Operating System.
Supports Windows, Mac, & Linux.
"""

import platform
import os
import subprocess


def openfile(f_path: str) -> None:
    """Open specified file based on detected Operating System.
    Supports Windows, Mac, & Linux.

    Args:
        f_path (str): Filepath for the file to be opened.
    """
    operating_system = platform.system()

    if operating_system == "Windows":
        os.startfile(f_path)
    else:
        if operating_system == "Darwin":
            subprocess.run(f'open "{f_path}"', shell=True)
        elif operating_system == "Linux":
            subprocess.run(f'xdg-open "{f_path}"', shell=True)
