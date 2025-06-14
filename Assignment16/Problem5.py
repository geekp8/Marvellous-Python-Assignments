def Lines():
    FileName=input()
    file = open(FileName, "r")  
    for line in file:
        words = line.strip().split()
        if len(words) > 5:
            print(line.strip())
    file.close()

def main():
    Lines()

if __name__ == "__main__":
    main()
