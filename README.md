# Combine-PDFs

Combines PDF files located in a folder in [USER]/Downloads

## Build Info

Windows

```bash
pyinstaller -F -n "Combine PDFs" --icon=.\icon\pdf.ico .\combinepdfs\main.py
```

MacOS

```bash
pyinstaller -F -n "Combine PDFs" ./combinepdfs/main.py
```

- Run Combine PDFs
- Drop \*.pdf files in *Combine_PDFs* folder located in ~/Downloads
  - Files are merged alphabetically (rename to reorder)
- Press *Enter* when prompted to merge and output
- Output file will be located in *Combine_PDFs* folder

Remove *-F* if having issues with Windows Defender, etc.
