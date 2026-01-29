
# Function to check whether a number is even or odd

num = int(input("Enter a number: "))

def even_odd(num):

    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

print ("The result is:", even_odd(num))  