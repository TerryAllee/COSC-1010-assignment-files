# Name:Terry Allee
# Date:September 22, 2024
# Budget Analysis Programming Project
# COSC 1010 DNT
#
# Use comments liberally throughout the program. 

# Function to calculate budget versus expenses
def budget_calculator():
    # Local variables
    # User inputs budget for the month
    budget = float(input("Enter your monthly budget:$"))
    total_expenses = 0.0
    # local variables used in calculations
    # User inputs expenses in a loop
    while True:
        expense = input("Enter your expenses:$")
        if expense.lower()=='done':
            break
        try:
            total_expenses += float(expense)
        except ValueError:
            print("Invalid entry. Enter a numeric value for the expense.")
    # local variables used for calculations
    # Calculate and display whether use is over or under budget
    if total_expenses > budget:
        print(f"You are over budget by ${total_expenses - budget:.2f}.")
    elif total_expenses < budget:
        print(f"You are under budget by ${budget - total_expenses:.2f}.")
    else:
        print("You are on budget! Exceptional Job staying on budget.")

# Call the function to run program
budget_calculator()
