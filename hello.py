import os
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
    print (full_path)