import os
import shutil
import sys

def CopyFiles(src_dir, dest_dir, extension):
    try:
        if not os.path.exists(src_dir):
            raise FileNotFoundError("Source directory does not exist.")

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        files_copied = 0
        for filename in os.listdir(src_dir):
            if filename.endswith(extension):
                src_path = os.path.join(src_dir, filename)
                dest_path = os.path.join(dest_dir, filename)
                shutil.copy(src_path, dest_path)
                print(f"Copied: {filename}")
                files_copied += 1

        if files_copied == 0:
            print(f"No files with extension {extension} found in {src_dir}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Use: DirectoryCopyExt.py <SourceDirectory> <TargetDirectory> <Extension>")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    extension = sys.argv[3]
    CopyFiles(src_dir, dest_dir, extension)

if __name__ == "__main__":
    main()
