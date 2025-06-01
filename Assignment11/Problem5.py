def CountZeroes(n):
    if n == 0:
        return 1
    def helper(n):
        if n == 0:
            return 0
        if n % 10 == 0:
            return 1 + helper(n // 10)
        else:
            return helper(n // 10)
    return helper(n)

def main():
    print("Enter a number:")
    num = int(input())
    result = CountZeroes(num)
    print("Number of zeroes:", result)

if __name__ == "__main__":
    main()
