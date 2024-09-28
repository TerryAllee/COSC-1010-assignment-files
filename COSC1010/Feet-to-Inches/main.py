#
# Name: Terry Allee
# Date: September 28th, 2024
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.


# Constant for inches per foot
INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    #Constant will convert feet to inches
    return feet * INCHES_PER_FOOT

# Main function
def main():
    # Declare a variable to store that asks for user input. 
    feet = float(input('Enter the number of feet: '))

    # Declare a variable that stores the result of the calculation.
    inches = feet_to_inches(feet)

    # Display the result
    print(f"{feet} foot or feet is equal to {inches} inches.")

# Call the main function.
main()
