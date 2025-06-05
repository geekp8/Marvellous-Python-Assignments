class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        print("Inside constructor")
        self.Name=Name
        self.Amount=Amount

    def Display(self):
        print("Inside display")
        print("Name is:",self.Name)
        print("Amount is:",self.Amount)

    def Deposit(self,depositAmt):
        self.Amount+=depositAmt

    def Withdraw(self,withdrawAmt):
        if withdrawAmt <=self.Amount:
            self.Amount-=withdrawAmt

    def CalculateInterest(self):
        interest=(self.Amount * BankAccount.ROI)/100
        print(f"Interest on {self.Amount} at ROI {BankAccount.ROI} % is:{interest}")
            
def main():
    obj1=BankAccount("Manasi",1000)
    obj1.Display()
    obj1.Deposit(500)
    obj1.Withdraw(300)
    obj1.CalculateInterest()
    obj1.Display()

    print("------------------------------------------------------------------")

    obj1=BankAccount("Alice",4000)
    obj1.Display()
    obj1.Deposit(1000)
    obj1.Withdraw(500)
    obj1.CalculateInterest()
    obj1.Display()



if __name__=="__main__":
    main()            
        

