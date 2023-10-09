"""

Searches for *.pdf files in "~User / Downloads / Merge_PDFs", 
merges them (in alphabetical order), and outputs a single "_MergedPDF.pdf" 
file to the same folder.

"""

from pathlib import Path

import PyPDF2


class CombinePDFs():
    """Combine pdf files in Merge_PDFs Folder"""

    def __init__(self) -> None:
        self.merge_folder = Path().home() / "Downloads" / "Merge_PDFs"
        self.files = []
        self.merger = PyPDF2.PdfMerger()
        # Create the directory if it doesn't exist
        if not self.merge_folder.is_dir():
            Path.mkdir(self.merge_folder)

    def get_files_from_dir(self):
        """Generate a list of files found in merge folder"""
        input(" Place PDFs in folder in order and press Enter...")
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
        self.merger.write(self.merge_folder / "_MergedPDF.pdf")
        self.merger.close()


go = CombinePDFs()
go.get_files_from_dir()
go.merge_files_from_dir()
go.write_merged_file()
