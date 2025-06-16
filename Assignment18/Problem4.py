# file: compare_files.py

import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

        if content1 == content2:
            print("Success: Both files have the same contents.")
        else:
            print("Failure: Files are different.")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
