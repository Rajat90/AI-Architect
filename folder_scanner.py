from pathlib import Path

SCAN_FOLDER = Path("invoices")

def scan_folder(folder):
    """
    Scnas a folder with mixed files types.
    Group files by extension.
    Reports what is found. 
    
     """
    all_files = list(folder.glob("*"))
    if not all_files:
        print("Folder is empty")
        return
    
    # Group files by extension
    grouped = {}

    for f in all_files:
        if f.is_file():
            ext = f.suffix.lower()
            if ext not in grouped:
                grouped[ext] = []
            grouped[ext].append(f.name)

    #Report
    print(f"Scan Report - {folder}")
    print(f"{"-"*40}")
    print(f"Total files found: {len(all_files)} files(s)")
    
    for ext, files in grouped.items():
        label = ext if ext else "(no extension)"
        print(f"{label} — {len(files)} file(s):")
        for name in files:
            print(f"    {name}")
        print()

if __name__ == "__main__":
    scan_folder(SCAN_FOLDER)
    