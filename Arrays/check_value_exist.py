#algorithm to check if a value exists in an array
numbers = [10, 20, 30, 40, 50]
target_number = 7
for number in  numbers:
    if number == target_number:
        print (f"value found: {target_number}")
    else :
        print (f"value not found: {target_number}")    