class Circle:
    PI=3.14 #class variable

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius=float(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.Area=Circle.PI * self.Radius* self.Radius

    def CalculateCircumference(self):
        self.Circumference= 2 * Circle.PI*self.Radius

    def Display(self):
        print("Radius of circle is:",self.Radius)     
        print("Circumference of circle is:",self.Circumference)
        print("Area of circle is:",self.Area)   

def main():
    circle1=Circle()
    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()

if __name__=="__main__":
    main()    