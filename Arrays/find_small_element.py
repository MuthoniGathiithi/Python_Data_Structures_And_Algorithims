#algorithim to find the smallest element in an array
numbers = [10, 20, 30, 40, 50]
minvalue = numbers[0]
for number in numbers:
    if number < minvalue:
        minvalue = number
print("The smallest element is:", minvalue)