import datetime

def add_expense():
    date = datetime.date.today()
    try:
        amount = float(input("Enter expense amount (₹): "))
    except ValueError:
        print(" Please enter a valid amount")
        return

    category = input("Enter category (Food / Travel / Other): ")
    note = input("Enter note (optional): ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")

    print(" Expense added successfully!")

def view_expenses():
    print("\n-- Your Expenses --")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount, category, note = line.strip().split(",")
                print(f"{date} | ₹{amount} | {category} | {note}")
    except FileNotFoundError:
        print("No expenses found!")

def main():
    while True:
        print("\n-- Hostel Expense Tracker --")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()
