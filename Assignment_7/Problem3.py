numbers=list(map(int,input("Enter list:").split()))
double=list(filter(lambda x:x%2==0,numbers))
print("Even Numbers:",double)