# file: copy_to_demo.py

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python copy_to_demo.py <source_file>")
        return

    source_file = sys.argv[1]
    destination_file = "Demo.txt"

    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            contents = src.read()
            dest.write(contents)
        print(f"Contents copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"File not found: {source_file}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
