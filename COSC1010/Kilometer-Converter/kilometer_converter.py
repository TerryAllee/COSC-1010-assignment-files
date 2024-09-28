#
# Name: Terry Allee
# Date: September 28, 2024
# Kilometer Conversion Programming Project
# COSC 1010

# Use comments liberally throughout the program.
 
# This program converts kilometers to miles
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls the show_miles function to convert it. 
def main ():
    # Get the distance in kilometers 
    kilometers = float (input('Enter a distance in kilometers:'))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from kilometers to miles and displays the result.
def show_miles (km):
    # Calculate the miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print (km, 'kilometers equals', miles, 'miles')

# Call the main function.
main()