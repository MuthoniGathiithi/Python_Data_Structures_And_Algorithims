#function to check whether a given value is present in a list

list = [90, 20, 35, 40, 55, 70]
value = int(input("Enter a value to check: "))

def check_value_in_list(list):
    if value in list:
        return f"{value} is present in the list."
    else:
        return f"{value} is not present in the list."

print(check_value_in_list(list))   