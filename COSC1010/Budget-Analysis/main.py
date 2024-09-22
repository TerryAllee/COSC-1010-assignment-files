# Name: Terry Allee 
# Date: September 22, 2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Function to calculate budget versus expenses
def budget_calculator():
    # Local variables
    # User inputs budget for the month
    budget = float(input("Enter your monthly budget: $"))
    total_expenses = 0.0
    # Local variables uses in calculations
    # User inputs expense in a loop until done
    while True:
        expense = input("Enter your expenses: $")
        if expense.lower() == 'done':
            break
        try:
            total_expenses =+ float(expense)
        except ValueError:
            print ("Invalid entry. Enter a value for your expense")
    # Local variables used for calculations
    # Calculate and display whether user is over or under budget
    if total_expenses > budget:
        print(f"You are over budget by ${total_expenses - budget:.2f}. Try to do better next month!")
    elif total_expenses < budget:
        print(f"You are under budget by ${budget - total_expenses:.2f}. You are under budget for the month! Exceptional JOB!")

# Call the function to run program
budget_calculator()

