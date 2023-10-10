# Combine-PDFs

Combines PDF files located in a folder in ~User / Downloads

## Installation 

- Create virtual environment and activate it

(Windows)

```bash
py -m venv env

.\env\Scripts\activate
```

(Mac/Linux)

```bash
python3 -m venv env

source env/bin/activate
```

- Install depencencies 

```bash
pip install -r requirements.txt
```

- Run combine_pdfs.py
- Drop .pdf files in *Combine_PDFs* folder located in ~/Downloads
  - Files are merged alphabetically (rename to reorder)
- Press *Enter* when prompted to merge and output
- Output file will be located in *Combine_PDFs* folder

## Windows executable build

```bash
pyinstaller --onefile --icon=.\combine-pdfs\icon\pdf_icon.ico .\combine-pdfs\combine_pdfs.py
```

(Remove *--onefile* if having issues with Windows Defender, etc. and see if that fixes the issue)

Windows executable will be located in *dist* folder
