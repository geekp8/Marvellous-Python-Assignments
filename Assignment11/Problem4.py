#Power=lambda a,b:a**b
def Power(a, b):
    if b == 0:
        return 1
    return a * Power(a, b - 1)


def main():
    print("Enter number:")
    no=int(input())
    print("Enter power:")
    no1=int(input())
    Result=Power(no,no1)
    print("Output is:",Result)


if __name__=="__main__":
    main()
