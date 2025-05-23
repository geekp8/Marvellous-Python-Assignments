from functools import reduce


numbers=list(map(int,input("Enter list:").split()))
product=list(reduce(lambda x,y:x * y,numbers))
print("Product:",product)