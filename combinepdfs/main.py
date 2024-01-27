"""

Searches for *.pdf files in the specified folder.
Defaults to: "[user]/Downloads/Merge_PDFs", 
Merges them (in alphabetical order), and outputs a single pdf 
file to the same folder.

"""

__version__ = "1.1.0"

from pathlib import Path
import PyPDF2

from modules.fileopen import openfile
from modules.art import art
from modules.settings import SETTINGS



class CombinePDFs():
    """Combine pdf files in Merge_PDFs Folder"""

    def __init__(self) -> None:
        
        self.merge_folder = SETTINGS["merge folder"]
        self.files = []
        self.merger = PyPDF2.PdfMerger()
        self.output_file = SETTINGS["output file"]
        
        # Create the directory if it doesn't exist
        try:
            if not self.merge_folder.is_dir():
                Path.mkdir(self.merge_folder, parents=True)
        except OSError:
            input(" Unable to create working folder. Verify filepath in settings.json.")
            exit()
            
        print(f"\n   V{__version__}{art}")

    def get_files_from_dir(self):
        """Generate a list of files found in merge folder"""
        print(" Place PDFs in the following folder and press Enter.\n",
            self.merge_folder)
        input()
        self.files = list(self.merge_folder.iterdir())

    def merge_files_from_dir(self):
        """Merges the files found in the generated list"""
        try:
            for file in self.files:
                self.merger.append(file)
                
        except PyPDF2.errors.DependencyError:
            input(" Unable to merge due to protected files")
        except PyPDF2.errors.PdfReadError:
            input(" Unable to merge. Verify all files are *.pdf")

    def write_merged_file(self):
        """Writes out the merged PDF file and closes the merger"""
        self.merger.write(self.output_file)
        self.merger.close()

    def open_output_file(self):
        """Opens the output file in the default application"""
        openfile(self.output_file)


go = CombinePDFs()

go.get_files_from_dir()
go.merge_files_from_dir()
go.write_merged_file()
go.open_output_file()
