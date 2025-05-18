number=int(input("Input:Number of elements:"))

nos=[]
for i in range(number):
    num=int(input("Input elements:"))
    nos.append(num)

x=int(input("Element to search:"))

freq=nos.count(x)

print("Output:",freq)
