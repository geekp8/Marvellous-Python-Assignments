import hashlib
import sys
import time
import os
import schedule


def CalculateCheckSum(path,BlockSize=1024):
    
    fobj=open(path,'rb')#read in binary

    hobj=hashlib.md5()
    
    buffer=fobj.read(BlockSize)
    while(len(buffer)>0):
       hobj.update(buffer)
       buffer=fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()


def DirectoryWatcher(DirectoryName="Marvellous"):

    flag=os.path.isabs(DirectoryName) #is absolute    
    if(flag==False):
        DirectoryName=os.path.abspath(DirectoryName)  

    flag=os.path.exists(DirectoryName)              

    if(flag==False):
        print("The path is invalid")
        exit()

    
    flag=os.path.isdir(DirectoryName)
    if(flag==False):
        print("Path is valid but the target is not Directory")
        exit()


    for FolderName,SubfolderNames,FileNames in os.walk(DirectoryName):
       
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)
            print("FileName: ",fname)
            print("Check sum ",checksum)
            print()
            
               
   

    timestamp=time.ctime()
    
    

    FileName="MarvellousLog%s.log" %(timestamp)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")
    #print(timestamp)
    fobj=open(FileName,"w")
    
    

    Border="-"*54

    fobj.write(Border+"\n")

    fobj.write("This is a log file of Marvellous Automation script\n")
    fobj.write("This is a directory cleaner script")
    fobj.write(Border+"\n")
    
    

    fobj.write(Border+"\n")
    
    fobj.write("This file is created at:\n"+timestamp+"\n")
    fobj.write(Border)


def FindDupicate(DirectoryName="Marvellous"):

    flag=os.path.isabs(DirectoryName) #is absolute    
    if(flag==False):
        DirectoryName=os.path.abspath(DirectoryName)  

    flag=os.path.exists(DirectoryName)              

    if(flag==False):
        print("The path is invalid")
        exit()

    
    flag=os.path.isdir(DirectoryName)
    if(flag==False):
        print("Path is valid but the target is not Directory")
        exit()

    Duplicate={}


    for FolderName,SubfolderNames,FileNames in os.walk(DirectoryName):
       
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:                
                Duplicate[checksum]=[fname]
            
    return Duplicate

def DisplayResult(MyDict):
    
    
    Result= list(filter(lambda x: len(x)>1,MyDict.values()))

    #print(Result)
    count=0

    for Value in Result:
        for subValue in Value:
            count=count+1
            print(subValue)
            
        print("------------------------------------------------")
        print("Value of count is:",count)
        print("-------------------------------------------------")
        count=0


def DeleteDuplicate(Path="Marvellous"):
    MyDict=FindDupicate(Path)

    Result= list(filter(lambda x: len(x)>1,MyDict.values()))

    #print(Result)
    count=0
    cnt=0

    for Value in Result:
        for subValue in Value:
            count=count+1
            if count>1:
                print("Deleted files: ",subValue)
                os.remove(subValue)
                cnt=cnt+1

            
        count=0
    print("Total deleted files: ",cnt)        


def main():
    Border="-"*54
    print(Border)
    print("------------Marvellous automation---------------------")
    print(Border)

    
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or (sys.argv[1]=="--H")):
            print("This application is used to perform Directory cleaning------")
            print("This is the Directory Automation script")
        elif(sys.argv[1]=="--u" or (sys.argv[1]=="--U")):
             print("Use the given script as ")
             print("Script name.py Name of directory")
             print("Please provide valid absolute path")
        else:
            #Result=FindDupicate(sys.argv[1])
            # #print(Result)
            # DeleteDuplicate(Result)
            #DeleteDuplicate()
            #print()
            schedule.every(1).minutes.do(DeleteDuplicate)

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid no of commandline arguments")
        print("Use the given flas as :")     
        print("--h: Used to display help")
        print("--u: Used to display the usage")        

    print(Border)
    print("--------Thankyou for using our Script-----------------")
    print("------------Marvellous Infosystems--------------------")
    print(Border)




if __name__=="__main__":
    main()