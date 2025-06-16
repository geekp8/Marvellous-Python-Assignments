import os
import sys

def RenameFiles(directory, old_ext, new_ext):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directory does not exist")

        for filename in os.listdir(directory):
            if filename.endswith(old_ext):
                base = filename.rsplit(old_ext, 1)[0]
                new_filename = base + new_ext
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Use: DirectoryRename.py <Directory> <OldExt> <NewExt>")
        return

    directory = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    RenameFiles(directory, old_ext, new_ext)

if __name__ == "__main__":
    main()
