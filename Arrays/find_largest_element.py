#algorithm to find the largest element in an array

numbers = [10, 20, 30, 40, 50]
maxvalue = numbers[0]
for number in numbers:
    if number > maxvalue:
        maxvalue = number
print("The largest element is:", maxvalue)