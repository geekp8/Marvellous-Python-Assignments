def Numbers():
       file = open("numbers.txt", "w")#checks if file is there else creates new note if already there it overwrites the content
       for i in range(10):
             num = input(f"Enter number {i+1}: ")
             file.write(num + "\n")
       file.close()

def main():
    Numbers()


if __name__=="__main__":
    main()    