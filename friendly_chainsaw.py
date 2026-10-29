import os
import shutil
import sys

# Core configuration for the cleanup target
TARGET_FILES = {
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    "npm-debug.log",
    "yarn-error.log",
}
TARGET_EXTENSIONS = {".log", ".tmp", ".bak", ".swp"}
TARGET_DIRS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints", ".sass-cache"}


def print_banner():
    """Prints a friendly ASCII art banner."""
    print("==================================================")
    print("        🪚  WELCOME TO FRIENDLY-CHAINSAW  🪚")
    print("==================================================")
    print("I will safely shred useless logs, caches, and empty folders.\n")


def clear_directory(target_path):
    """Scans and cleans the target directory recursively."""
    if not os.path.exists(target_path):
        print(f"❌ Error: The path '{target_path}' does not exist.")
        return

    print(f"🔍 Scanning: {os.path.abspath(target_path)}")
    deleted_files_count = 0
    deleted_dirs_count = 0
    saved_space = 0

    # Step 1: Walk through and destroy target files and cache directories
    for root, dirs, files in os.walk(target_path, topdown=False):
        # Clean specific directory caches
        for directory in dirs:
            if directory in TARGET_DIRS:
                full_dir_path = os.path.join(root, directory)
                try:
                    # Calculate size before deleting
                    for path, _, filenames in os.walk(full_dir_path):
                        for f in filenames:
                            saved_space += os.path.getsize(os.path.join(path, f))

                    shutil.rmtree(full_dir_path)
                    print(f"🪚 [SHREDDED DIR]  -> {full_dir_path}")
                    deleted_dirs_count += 1
                except Exception as e:
                    print(f"⚠️ [SKIP DIR]      -> {full_dir_path} (Reason: {e})")

        # Clean junk files
        for file in files:
            _, ext = os.path.splitext(file)
            if file in TARGET_FILES or ext.lower() in TARGET_EXTENSIONS:
                full_file_path = os.path.join(root, file)
                try:
                    saved_space += os.path.getsize(full_file_path)
                    os.remove(full_file_path)
                    print(f"🪚 [SHREDDED FILE] -> {full_file_path}")
                    deleted_files_count += 1
                except Exception as e:
                    print(f"⚠️ [SKIP FILE]     -> {full_file_path} (Reason: {e})")

    # Step 2: Second pass to safely remove completely empty folders
    print("\n🌿 Pruning empty branches...")
    for root, dirs, _ in os.walk(target_path, topdown=False):
        for directory in dirs:
            full_dir_path = os.path.join(root, directory)
            try:
                # Check if directory is entirely empty
                if not os.listdir(full_dir_path):
                    os.rmdir(full_dir_path)
                    print(f"✨ [PRUNED EMPTY]  -> {full_dir_path}")
                    deleted_dirs_count += 1
            except Exception:
                pass

    # Summary Display
    print("\n==================================================")
    print("               ✨ CLEANUP COMPLETE ✨")
    print("==================================================")
    print(f"Files Shredded   : {deleted_files_count}")
    print(f"Folders Pruned   : {deleted_dirs_count}")
    print(f"Space Reclaimed  : {saved_space / 1024:.2f} KB")
    print("==================================================")


if __name__ == "__main__":
    print_banner()

    # Allows drag-and-drop or argument input via terminal
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("👉 Enter the full folder path to clean up: ").strip()

    # Safe validation check to prevent accidental root or system drive deletion
    resolved_path = os.path.abspath(target)
    if resolved_path in [os.path.abspath("/"), os.path.abspath(".")] or len(
        target
    ) < 3:
        confirm = (
            input(
                f"🚨 Warning: You selected '{target}'. Are you sure you want to run the chainsaw here? (yes/no): "
            )
            .strip()
            .lower()
        )
        if confirm != "yes":
            print("❌ Operation cancelled. The friendly chainsaw remains idle.")
            sys.exit()

    clear_directory(target)
