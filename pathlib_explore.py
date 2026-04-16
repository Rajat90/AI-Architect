from pathlib import Path

# --- Block 1: Basic Path object ---
p = Path("invoices")
print(type(p))          # What type is it?
print(p.exists())       # Does the folder exist?
print(p.is_dir())       # Is it a directory?

# --- Block 2: Path joining with / ---
invoice = p / "INV001.txt"
print(invoice)
print(invoice.exists())
print(invoice.name)     # Full filename
print(invoice.stem)     # Without extension
print(invoice.suffix)   # Just extension
print(invoice.parent)   # Parent folder

# --- Block 3: glob() — find files by pattern ---
txt_files = list(p.glob("*.txt"))
print(f"Found {len(txt_files)} .txt files:")
for f in txt_files:
    print(f"  {f.name}")