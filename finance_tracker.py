def add_expense(data):
    """Add a new expense to the data dictionary."""
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if category not in data:
            data[category] = []
        data[category].append((description, amount))
        print("Expense added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_expenses(data):
    """Display all expenses categorized."""
    if not data:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amount in expenses:
            print(f"  - {desc}: ${amount:.2f}")

def view_summary(data):
    """Display total amount spent per category."""
    if not data:
        print("No expenses recorded yet.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    print("Welcome to the Personal Finance Tracker!")
    data = {}

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
