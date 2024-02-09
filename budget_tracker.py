class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, amount, category, transaction_type):
        if transaction_type.lower() == 'income':
            self.balance += amount
        elif transaction_type.lower() == 'expense':
            self.balance -= amount
        else:
            print("Invalid transaction type. Use 'income' or 'expense'.")
            return

        transaction = {'amount': amount, 'category': category, 'type': transaction_type}
        self.transactions.append(transaction)
        print(f"{transaction_type.capitalize()} of ${amount} in {category} added successfully.")

    def view_balance(self):
        print(f"Current Balance: ${self.balance}")

    def view_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(f"{transaction['type'].capitalize()} of ${transaction['amount']} in {transaction['category']}")

# Example usage
if __name__ == "__main__":
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Add Transaction")
        print("2. View Balance")
        print("3. View Transactions")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            transaction_type = input("Enter the transaction type (income/expense): ")
            budget_tracker.add_transaction(amount, category, transaction_type)

        elif choice == '2':
            budget_tracker.view_balance()

        elif choice == '3':
            budget_tracker.view_transactions()

        elif choice == '4':
            print("Exiting the Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
