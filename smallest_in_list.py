# Program to find the smallest number in a list

numbers = [12, 45, 23, 67, 34, 89, 10]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)