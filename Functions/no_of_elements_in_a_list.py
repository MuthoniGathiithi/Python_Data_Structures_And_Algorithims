
# Function to count the number of elements in a list without using len()

list = [40,30,590,20,500,4000]


def count_elements(list):
  
    total_elements = 0
    for number in list:
        total_elements += 1
    return total_elements

print("The total number of elements in the list is:", count_elements(list))