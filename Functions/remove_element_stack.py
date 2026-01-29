# Function to remove the top element from a stack (list) and return the updated stack


list = [303,50.89,79]

def remove_element(list):
    list.pop()
    return list
print("Updated stack after removing element:", remove_element(list))
