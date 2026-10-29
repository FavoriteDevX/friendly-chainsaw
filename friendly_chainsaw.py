import os
import shutil
import sys
import time

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
    """Prints a custom ASCII art banner inspired by the user's chainsaw image."""
    print("==========================================================================")
    print("                      WELCOME TO FRIENDLY-CHAINSAW                        ")
    print("==========================================================================")
    print("         ____                                                             ")
    print("      _/_||_\\_                                                            ")
    print("     //   __   \\      _________________________________________________   ")
    print("    ||  [____]  ||===| o o                                            |   ")
    print("     \\\\________//     \\_______________________________________________|   ")
    print("      \\________/                                                          ")
    print("==========================================================================")
    print("I will safely shred useless logs, caches, and empty folders.\n")


def animate_chainsaw(text, action_label):
    """Animates a text chainsaw slicing through the text path in real-time."""
    max_len = 45
    if len(text) > max_len:
        text = "..." + text[-(max_len - 3) :]

    padding = " " * 4
    full_string = f"{padding}[{action_label}] {text}"
    str_len = len(full_string)

    # Animates the slice movement using a mini text-chainsaw text representation: o===[>
    for i in range(str_len + 1):
        left_side = full_string[:i]
        right_side = full_string[i:]
        sys.stdout.write(f"\r{left_side}o===[>{right_side}")
        sys.stdout.flush()
        time.sleep(0.01)

    sys.stdout.write(f"\r{full_string} *SHREDDED!*\n")
    sys.stdout.flush()
    time.sleep(0.04)


def clear_directory(target_path):
    """Scans and cleans the target directory recursively with animations."""
    if not os.path.exists(target_path):
        print(f"❌ Error: The path '{target_path}' does not exist.")
        return

    print(f"🔍 Scanning: {os.path.abspath(target_path)}\n")
    deleted_files_count = 0
    deleted_dirs_count = 0
    saved_space = 0

    # Step 1: Walk through and destroy target files and cache directories
    for root, dirs, files in os.walk(target_path, topdown=False):
        for directory in dirs:
            if directory in TARGET_DIRS:
                full_dir_path = os.path.join(root, directory)
                try:
                    for path, _, filenames in os.walk(full_dir_path):
                        for f in filenames:
                            saved_space += os.path.getsize(os.path.join(path, f))

                    animate_chainsaw(directory, "DIR")
                    shutil.rmtree(full_dir_path)
                    deleted_dirs_count += 1
                except Exception:
                    pass

        for file in files:
            _, ext = os.path.splitext(file)
            if file in TARGET_FILES or ext.lower() in TARGET_EXTENSIONS:
                full_file_path = os.path.join(root, file)
                try:
                    saved_space += os.path.getsize(full_file_path)
                    animate_chainsaw(file, "FILE")
                    os.remove(full_file_path)
                    deleted_files_count += 1
                except Exception:
                    pass

    # Step 2: Second pass to safely remove completely empty folders
    print("\n🌿 Pruning empty branches...")
    time.sleep(0.5)
    for root, dirs, _ in os.walk(target_path, topdown=False):
        for directory in dirs:
            full_dir_path = os.path.join(root, directory)
            try:
                if not os.listdir(full_dir_path):
                    animate_chainsaw(directory, "PRUNE")
                    os.rmdir(full_dir_path)
                    deleted_dirs_count += 1
            except Exception:
                pass

    # Summary Display
    print("\n==========================================================================")
    print("                               CLEANUP COMPLETE                           ")
    print("==========================================================================")
    print(f"Files Shredded   : {deleted_files_count}")
    print(f"Folders Pruned   : {deleted_dirs_count}")
    print(f"Space Reclaimed  : {saved_space / 1024:.2f} KB")
    print("==========================================================================")


if __name__ == "__main__":
    print_banner()

    if len(sys.argv) > 1:
        target = sys.argv
    else:
        target = input("👉 Enter the full folder path to clean up: ").strip()

    resolved_path = os.path.abspath(target)
    if resolved_path in [os.path.abspath("/"), os.path.abspath(".")] or len(
        target
    ) < 3:
        confirm = (
            input(
                f"🚨 Warning: Run chainsaw on '{target}'? (yes/no): "
            )
            .strip()
            .lower()
        )
        if confirm != "yes":
            print("❌ Operation cancelled. The friendly chainsaw remains idle.")
            sys.exit()

    clear_directory(target)
