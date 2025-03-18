
##a. Ask the user to input three numbers, and check if these three numbers can form a triangle. 
    ##  Need three inputs. 
    ## T he output shows whether the result can form a triangle or not.

# check for triangle 
def check_triangle(a, b, c):
   return a + b > c and a + c > b and b + c > a

# Function to process user input for check int, float , char
def check_input(user_input):
    try:

        if user_input.isdigit():
            return int(user_input)
        
   
     # Try converting to float
        float_number = float(user_input)
        int_number = round(float_number, 0)
        print(f"User input number {user_input} is converted to integer number {int_number}")
        return int_number
    
    except ValueError:
         # If input value is  character
        ascii_value = [ord(char) for char in user_input]
        print(f"User input character  {user_input} is converted to ascii value {ascii_value}")
        int_number = sum(ascii_value)
        if type(int_number) == int:
            return int_number
        else: 
            return 0
           


# Taking user inputs
a = check_input(input("Please enter first side of Triangle : "))
b = check_input(input("Please enter second side of Triangle : "))
c = check_input(input("Please enter Third side of Triangle : "))
print(f"a = {a} ")
print(f"b = {b} ")
print(f"c = {c} ")


#### lets check the result
if check_triangle(a, b, c):
    print("Yes, these three lengths can form a triangle. ") 
else:
    print("'No, these three lengths cannot form a triangle. ") 

