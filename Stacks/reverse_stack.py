#algorithm to reverse a string using a stack
text = "hello"

stack = []

for char in text:
    stack.append(char)  # Push each character onto the stack

reversed_text = ""
while stack:
    reversed_text += stack.pop()  # Pop characters from the stack to form reversed string   


print("Reversed string is:", reversed_text)        
