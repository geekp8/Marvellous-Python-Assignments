def printTriangle(n, current=1):
    if current > n:
        return
    print("* " * current)
    printTriangle(n, current + 1)

def main():
    #print("Enter number of rows:")
    n = 4
    printTriangle(n)

if __name__ == "__main__":
    main()
