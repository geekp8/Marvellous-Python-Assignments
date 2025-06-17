import os
import hashlib
import sys

def CalCheckSum(filepath):
    hobj = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hobj.update(byte_block)
        return hobj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def Processdirectory(directory):
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    print(f"\nChecksums for files in directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            checksum = CalCheckSum(filepath)
            print(f"{filepath} -> {checksum}")

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryChecksum.py \"<DirectoryName>\"")
        return

    directory = sys.argv[1]
    Processdirectory(directory)

if __name__ == "__main__":
    main()
