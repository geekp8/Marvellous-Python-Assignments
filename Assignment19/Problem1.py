import os
import sys

def SearchFiles(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directory does not exist")

        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        print(f"Files with extension {extension}:")
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Use: DirectoryFileSearch.py <Directory> <Extension>")
        return

    directory = sys.argv[1]
    extension = sys.argv[2]
    SearchFiles(directory, extension)

if __name__ == "__main__":
    main()
