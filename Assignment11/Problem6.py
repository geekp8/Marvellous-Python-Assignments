def SumNatural(n):
    if n == 0:
        return 0
    return n + SumNatural(n - 1)

def main():
    print("Enter a number:")
    n = int(input())
    result = SumNatural(n)
    print("Sum of first", n, "natural numbers is:", result)

if __name__ == "__main__":
    main()
