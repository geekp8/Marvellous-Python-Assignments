# file: copy_to_demo.py

import sys

def main():
    
    
    file=open('Source.txt','r')
    #print("Opened the file",file)

    #source_file = "Source.txt"
    destination_file = "Destination.txt"

    try:
        with open(file, 'r') as src, open(destination_file, 'w') as dest:
            contents = src.read()
            dest.write(contents)
        print(f"Contents copied from {file} to {destination_file}")
    except FileNotFoundError:
        print(f"File not found: {file}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
