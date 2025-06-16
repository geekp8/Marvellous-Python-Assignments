import os

def main():
    print("Enter the name of the file that you want to check: ")
    FileName=input()

    ret=os.path.exists(FileName)#exists to check whether the file is there or not

    if (ret==True):
        print("File is present in the current directory")
    else:
        print("There is no such file")


if __name__=="__main__":
    main()   
