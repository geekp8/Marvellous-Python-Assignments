class BookStore:
    NoOfBooks=0 #class variable

    def __init__(self,Name,Author):
        print("Inside constructor")
        self.Name=Name #instance variable
        self.Author=Author
        BookStore.NoOfBooks+=1#increment this use name of class 

    def Display(self):
        print("Inside display")
       
        #instead of 3 diff prints use one

        print(f"{self.Name} by {self.Author} .No of books:{BookStore.NoOfBooks}")
            
def main():
    obj1=BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()


if __name__=="__main__":
    main()            
        

