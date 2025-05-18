no=int(input("Enter number of elements:"))

List=[]

for i in range(no):
    num=int(input("Enter element:" + str(i+1)))
    List.append(num)

print("Output:",sum(List))    


