#algorithm to reverse an array  without using method reverse()
numbers = [10, 20, 30, 40, 50]
reversed_numbers = []

for number in numbers:

    reversed_numbers.insert(0, number)
print("Reversed array is:", reversed_numbers)
