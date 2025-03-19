"""
 a. Ask the user to input three numbers, and check if these three numbers can form a triangle. 
    ## Need three inputs. 
    ## The output shows whether the result can form a triangle or not.
"""

# default side length
default_length = 0
# deafult rounding precision
default_round_precision = 2

""" 
Check if the three sides can form a triangle. 

Returns true if either of the two sides combined are longer than the third side; false otherwise.
"""
def check_triangle(a, b, c):
   return a + b > c and a + c > b and b + c > a

"""
Function to scrub user inputs (allows for int, float, and numeric string inputs)

An int input is returned as-is
A float input is rounded to its {default_round_precision} decimal places
A single-char input is converted to its ASCII equivalent
For more than two chars, the sum of the ASCII values of each char is used

For invalid inputs, we default to {default_length}
"""
def scrub_input(user_input):
    try:

        if user_input.isdigit():
            return int(user_input)
   
        # Try converting to float
        float_number = float(user_input)
        rounded_number = round(float_number, default_round_precision)

        print(f"User input number {user_input} has been rounded to {rounded_number}")

        return rounded_number
    
    except ValueError:

         # If input value is character
        ascii_value = [ord(char) for char in user_input]
        int_number = sum(ascii_value)

        print(f"User input character {user_input} is converted to ascii value {int_number}")

        if type(int_number) == int:
            return int_number
        else: 
            print (f"User input character {user_input} is invalid. Defaulting to side length {default_length}")
            return default_length

# Taking user inputs
a = scrub_input(input("Please enter first side of Triangle : "))
b = scrub_input(input("Please enter second side of Triangle : "))
c = scrub_input(input("Please enter Third side of Triangle : "))

print(f"a = {a} ")
print(f"b = {b} ")
print(f"c = {c} ")

#### lets check the result
if check_triangle(a, b, c):
    print("Yes, these three lengths can form a triangle. ") 
else:
    print("No, these three lengths cannot form a triangle. ") 