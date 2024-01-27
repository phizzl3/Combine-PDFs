"""

Searches for *.pdf files in "~User / Downloads / Merge_PDFs", 
merges them (in alphabetical order), and outputs a single "_MergedPDF.pdf" 
file to the same folder.

"""

__version__ = "1.0.0"

from pathlib import Path
import PyPDF2

from utils.fileopen import openfile
from utils.art import art


WORKING_FOLDER = "Combine_PDFs"
OUTPUT_FILE = "_Merged_PDF.pdf"


class CombinePDFs():
    """Combine pdf files in Merge_PDFs Folder"""

    def __init__(self) -> None:
        self.merge_folder = Path().home() / "Downloads" / WORKING_FOLDER
        self.files = []
        self.merger = PyPDF2.PdfMerger()
        self.output_file = self.merge_folder / OUTPUT_FILE
        # Create the directory if it doesn't exist
        if not self.merge_folder.is_dir():
            Path.mkdir(self.merge_folder)
        print(f"\n  V{__version__}{art}")

    def get_files_from_dir(self):
        """Generate a list of files found in merge folder"""
        input(
            f" Place PDFs in *{WORKING_FOLDER}* folder located in: ~/Downloads and press Enter...")
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
