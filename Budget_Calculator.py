# Define a class for the budget calculator
class BudgetCalculator:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    # Method to get user's monthly income
    def get_income(self):
        self.income = float(input("Enter your monthly income: $"))

    # Method to add an expense to the budget
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    # Method to calculate the remaining budget
    def calculate_budget(self):
        total_expenses = sum(self.expenses.values())
        remaining_budget = self.income - total_expenses
        return remaining_budget

    # Method to display the budget summary
    def display_budget(self):
        print("\nBudget Summary:")
        print(f"Monthly Income: ${self.income}")
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
        remaining_budget = self.calculate_budget()
        print(f"Remaining Budget: ${remaining_budget:.2f}")

# The main function to run the budget calculator
def main():
    calculator = BudgetCalculator()  # Create an instance of the BudgetCalculator class
    calculator.get_income()  # Get the user's income

    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. Calculate budget")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input(f"Enter expense amount for {category}: $"))
            calculator.add_expense(category, amount)  # Add an expense to the budget
        elif choice == "2":
            calculator.display_budget()  # Calculate and display the budget
        elif choice == "3":
            print("Exiting the budget calculator.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Entry point to run the program
if __name__ == "__main__":
    main()
