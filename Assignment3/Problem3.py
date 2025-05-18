def Minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

n = int(input("Input:Number of elements: "))
numbers = []

print("Input elements:")
for _ in range(n):
    numbers.append(int(input()))


minno = Minimum(numbers)
print("Output:", minno)
