# Function to find the maximum value in a list of numbers


list = [40,30,590,20,500,4000]
max_number = list[0]

def find_max_number(list ,max_number ):
    for number in list:
        if number > max_number:
            max_number = number
    return max_number 
print("The maximum number is:", find_max_number(list,max_number))
