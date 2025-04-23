
# b. Ask users to input one number, the number will be the size of a square. Using the print 
# function to draw this square. 
#  Need input size. 
#  The output will be a single square created by the print function.

def create_square(size):
    for row in range(size):
        # for col in range(size):
         if row == 0 or row == size - 1:
            #  print('*', row, end=' ')
             print('* ' * (size))
         else:
                print('* ' + '  ' *(size-2) + '*'  )
           

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
            print("please enter valid number for create square")
           


# Taking user inputs
size = check_input(input("Please enter size of square : "))
# create square
print("size = ", size)
create_square(size)

