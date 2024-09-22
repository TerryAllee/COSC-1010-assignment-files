#
# Name: Terry Allee
# Date: September 22, 2024
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
total = 0

# Get number of bugs collected each day using a for loop.
for day in range (1,6):
    # user enters bugs collected today
    print('Enter bugs collected today', day)

    # Enter the number of bugs.
    bugs = int(input())

    # Add the bugs up
    total += bugs

# Display the total number of bugs collected.
print ('Your total bugs collected', total, 'bugs')
