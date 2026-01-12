import pandas as pd
from datetime import date

FILE = "expenses.csv"

def add_expense():
    category = input("Category (Food, Travel, etc): ")
    amount = float(input("Amount: "))
    note = input("Note: ")

    new_data = {
        "Date": date.today(),
        "Category": category,
        "Amount": amount,
        "Note": note
    }

    df = pd.read_csv(FILE)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(FILE, index=False)

    print("Expense added successfully!\n")

def show_summary():
    df = pd.read_csv(FILE)

    print("\nTotal Expense:", df["Amount"].sum())

    print("\nCategory-wise Summary:")
    print(df.groupby("Category")["Amount"].sum())

    print("\nHighest Expense:")
    print(df.loc[df["Amount"].idxmax()])

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
