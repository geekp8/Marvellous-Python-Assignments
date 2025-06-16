import os
import shutil
import sys

def CopyFiles(src_dir, dest_dir):
    try:
        if not os.path.exists(src_dir):
            raise FileNotFoundError("Source directory does not exist")

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for filename in os.listdir(src_dir):
            full_file_name = os.path.join(src_dir, filename)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_dir)
                print(f"Copied: {filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Use: DirectoryCopy.py <SourceDirectory> <TargetDirectory>")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    CopyFiles(src_dir, dest_dir)

if __name__ == "__main__":
    main()
