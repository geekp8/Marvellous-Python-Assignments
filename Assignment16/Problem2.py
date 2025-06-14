def main():

    with open('data.txt','r') as file:
        fobj=file.read()
        print(fobj)

if __name__=="__main__":
    main()