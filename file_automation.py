# ============================================
# File Automation — OS Module Exploration
# ============================================

import os

# 1. Where are we right now?
current_folder = os.getcwd()
print(f"📍 Current folder: {current_folder}")
print()

# 2. What files and folders are here?
print("📁 Contents of current folder:")
contents = os.listdir(".")    # "." means current folder
for item in contents:
    print(f"   {item}")
print()

# 3. What's inside bot_logs folder?
print("📁 Contents of bot_logs folder:")
log_files = os.listdir("bot_logs")
for file in log_files:
    print(f"   {file}")
print()

# 4. Does a specific file exist?
file_to_check = "bot_logs/vertrag_log.txt"
if os.path.exists(file_to_check):
    print(f"✅ File exists: {file_to_check}")
else:
    print(f"❌ File not found: {file_to_check}")
print()

# 5. Is something a file or a folder?
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"  📄 FILE   : {item}")
    elif os.path.isdir(item):
        print(f"  📁 FOLDER : {item}")


# ============================================
# Find only .txt files in bot_logs folder
# ============================================

print()
print("=" * 45)
print("🔍 SCANNING FOR LOG FILES...")
print("=" * 45)

log_folder = "bot_logs"
all_items  = os.listdir(log_folder)

# Filter only .txt files
txt_files = []
for item in all_items:
    if item.endswith(".txt"):        # ← checks file extension
        txt_files.append(item)

print(f"Found {len(txt_files)} log files:")
for filename in txt_files:
    # Build the full path — folder + filename
    full_path = os.path.join(log_folder, filename)
    #           ↑
    #   os.path.join safely combines paths
    #   works on Windows AND Mac/Linux
    #   never use "folder" + "/" + "file" manually!
    
    file_size = os.path.getsize(full_path)
    print(f"  📄 {filename:<30} ({file_size} bytes)")


# ============================================
# Read every log file automatically
# ============================================

print()
print("=" * 55)
print("📂 READING ALL LOG FILES...")
print("=" * 55)

all_log_entries = []   # will store ALL entries from ALL files

for filename in txt_files:
    full_path = os.path.join(log_folder, filename)
    
    # Read this file
    with open(full_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    print(f"\n📄 {filename} — {len(lines)} entries")
    print("-" * 45)
    
    # Process each line
    for line in lines:
        parts     = line.strip().split(" | ")
        bot_name  = parts[0]
        timestamp = parts[1]
        error     = parts[2]
        
        # Store as dictionary for easy access later
        entry = {
            "bot"       : bot_name,
            "timestamp" : timestamp,
            "error"     : error,
            "source"    : filename    # which file it came from
        }
        all_log_entries.append(entry)
        
        print(f"  {bot_name:<15} | {error}")

print()
print("=" * 55)
print(f"✅ Total entries loaded: {len(all_log_entries)}")