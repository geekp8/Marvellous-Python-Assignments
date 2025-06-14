def main():
    print("Enter the Name of the File that you want to create:")
    FileName=input()

    fobj=open(FileName,'w')
    print("Enter the data to write in file:")
    data=input()


    fobj.write(data)

    fobj.close()

if __name__=="__main__":
    main()
