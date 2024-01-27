# Combine-PDFs

Combines PDF files located in a specified folder.  
Defaults to: *[USER]/Downloads/Combine_PDFs*

## Build Info

Windows

```bash
pyinstaller -F -n "Combine PDFs" --icon=.\icon\pdf.ico .\combinepdfs\main.py
```

Remove *-F* if having issues with Windows Defender, etc.

MacOS

```bash
pyinstaller -F -n "Combine PDFs" ./combinepdfs/main.py
```

- Run Combine PDFs
- Drop \*.pdf files in *Combine_PDFs* folder located in ~/Downloads
  - Files are merged alphabetically (rename to reorder)
- Press *Enter* when prompted to merge and output
- Output file will be located in *Combine_PDFs* folder

### Settings

- Creates a settings.json file at [USER]/PyAppFiles/Combine PDfFs/settings.json
- Update this file to adjust file path info
- Sample json file included in package /json folder
