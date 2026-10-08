import json
from datetime import date
today = date.today().isoformat()



expenses=[]
def load_expenses():
    global expenses

    try:
        with open("expenses.json","r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)



def add_expense():
    while True:
        amount = input("Amount: ")

        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")
    while True:
        category = input("Category: ").strip()

        if category:
         break

        print("Category cannot be empty.")

    while True:
        description = input("Description: ").strip()

        if description:
            break

        print("Description cannot be empty.")
    if expenses:
        new_id = max(expense["ID"] for expense in expenses) + 1
    else:
        new_id = 1

    expense={
            "ID":new_id,
            "amount":amount,
            "category":category,
            "description":description,
            "date": today
   }

    expenses.append(expense)
    save_expenses()

    print("expenses added successfully")



def view_expenses():
    print("\n========== EXPENSES ==========")
    for expense in expenses:
        print(
            f"ID: {expense["ID"]} |" 
            f"Amount: {expense['amount']} |" 
            f"Category: {expense['category']} |" 
            f"Description: {expense['description']}"

        )

def search_expense():
    category = input("Enter category to search: ").lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"ID: {expense['ID']} | "
                f"₹{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )
            found = True

    if not found:
        print("No expenses found.")


def delete_expenses():
    try:
        expense_id=int(input("Enter expense ID to delete:"))
        for expense in expenses:
            if expense["ID"] == expense_id:
                expenses.remove(expense)
                print("expenses removed successfully")
                return
        print("expenses not found.")

    except ValueError:
        print("please enter a vaild ID")

def total_expenses():
    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print(f"Total spending: ₹{total:.2f}")
def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")
load_expenses()

while True:
    print("=========================")
    print("    EXPENSE TRACKER")
    print("=========================")

    print("1. Add Expense")
    print('2. View Expenses')
    print('3.delete Expenses')
    print("4.Search Expense")
    print("5.Total Spending")
    print("6.Category Summary")
    print("7.Exit")

    choice = input("Enter Your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expenses()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        total_expenses()
    elif choice == "6":
        category_summary()
    elif choice=="7":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")







