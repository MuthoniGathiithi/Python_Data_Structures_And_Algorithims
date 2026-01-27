stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print (stack.pop())  # Outputs: 3
print (stack[-1])
print (len(stack) )  # Outputs: False
reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())
print("Reversed stack is:", reversed_stack)
#algorithm to reverse an array  without using method reverse()
