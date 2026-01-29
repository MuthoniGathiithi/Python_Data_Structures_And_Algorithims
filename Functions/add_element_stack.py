# function to add an element to a stack (list)

list = [303,50.89,79]

def add_element_stack(list):
    element = input("Enter an element to add to the stack: ")
    list.append(element)
    return list
print("Updated stack:", add_element_stack(list))