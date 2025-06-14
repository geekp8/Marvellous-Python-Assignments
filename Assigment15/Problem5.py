# file: compare_files.py

import sys

def main():
    if len(sys.argv) != 3:
        print("Check for frequency of word from System line argument")
        return

    file1 = sys.argv[1]
    searchInput=sys.argv[2]

    try:
        with open(file1, "r") as file:
            content = file.read()
            frequency = content.count(searchInput)

            print(f"The string '{searchInput}' appears {frequency} times in the file.")
        
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()



