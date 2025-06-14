def Lines():
    FileName=input("Enter name of the file:")
    file = open(FileName, "r")  
    
    fobj=file.readlines()
    #print(fobj)
    linecount=len(fobj)
    wordcount=0
    charcount=0

    for line in fobj:
        wordcount=wordcount+len(line.split())
        charcount=charcount+len(line)
    print("Lines count:",linecount)
    print("Word count:",wordcount)
    print("Characters Count:",charcount)
    
    file.close()

def main():
    Lines()

if __name__ == "__main__":
    main()
