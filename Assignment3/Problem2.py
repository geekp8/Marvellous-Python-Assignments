def Maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

n = int(input("Enter the number of elements: "))
numbers = []

print("Enter the numbers:")
for _ in range(n):
    numbers.append(int(input()))


maxno = Maximum(numbers)
print("The maximum number is:", maxno)
