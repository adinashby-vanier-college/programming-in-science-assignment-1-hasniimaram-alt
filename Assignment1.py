# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    return max(num1, num2, num3)
   

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return min(num1, num2, num3) 
    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        return "Positive"
    if number == 0:
        return "Zero"
    if number < 0:
        return "Negative"
   

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    result =""
    for i in range(rows + 1):
        result += "*" * i + "\n"
    return result.strip("\n")

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    num = 1
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip() 

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)
print(sum_of_even_numbers(1,10))