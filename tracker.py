import csv
import os
from datetime import datetime

FILE_NAME = "expense.csv"

def init_file():
    """Create file with header if it dones not exit"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    category = input("Enter category (Food, Rent, Travel, Other): ").strip()
    description = input("Enter description: ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expense():
    if not os.path.exists(FILE_NAME):
        print("No expense found.")
        return
    
    with open(FILE_NAME, mode="r") as f:
        reader = csv.reader(f)
        next(reader) #Skip header
        print("\n--- Your expense ---")
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expense found")
        return
    
    total = 0
    with open(FILE_NAME, mode="r") as f:
        reader = csv.reader(f)
        next(reader) #Skip header
        for row in reader:
            print("Value:", row[3])
            total += float(row[3])

    print(f"\nTotal expense: {total:.2f}")


def main():
    init_file()
    while True:
        print("\n\n--- Choose expense tracker option ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. or type exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice.lower() in ['4', 'exit']:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
