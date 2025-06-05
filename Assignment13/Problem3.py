class Numbers:
    #Value=0

    def __init__(self,Value):
        print("Inside constructor")
        self.Value=Value
        

    def ChkPrime(self):
        if self.Value<=1:
            return False
        for i in range(2,int(self.Value ** 0.5)+1):
            if self.Value % i==0:
                return False
        return True

    def SumFactors(self):
        sumFactors=0
        for i in range(1,self.Value):
            if self.Value % i==0:
                sumFactors+=i
        return sumFactors


    def ChkPerfect(self):
        return self.SumFactors()==self.Value


    def Factors(self):
        print(f"Factors of {self.Value} are:")
        for i in range(1,self.Value):
            if self.Value % i==0:
                print(i,end=' ')
        print()


def main():
    num1=Numbers(28)
    num2=Numbers(12)
    num3=Numbers(10)

    num1.Factors()
    print("Is the no perfect:",num1.ChkPerfect())
    print("Is the no prime:",num1.ChkPrime())
    num1.SumFactors()

    num2.Factors()
    print("Is the no perfect:",num2.ChkPerfect())
    print("Is the no prime:",num2.ChkPrime())
    num2.SumFactors()


    num3.Factors()
    print("Is the no perfect:",num3.ChkPerfect())
    print("Is the no prime:",num3.ChkPrime())
    num3.SumFactors()

if __name__=="__main__":
    main()    

       

  