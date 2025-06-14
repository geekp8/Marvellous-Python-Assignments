def remove_blank_lines(input_file, output_file):
    infile = open(input_file, "r")
    outfile = open(output_file, "w")
    
    for line in infile:
        if line.strip() != "":
            outfile.write(line)
    
    infile.close()
    outfile.close()

def main():
    remove_blank_lines("input.txt", "cleaned.txt")

if __name__ == "__main__":
    main()
