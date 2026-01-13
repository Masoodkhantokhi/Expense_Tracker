# Expense Tracker Project

expensesList = []

print("Welcome to Expense Tracker: ")
print("Expense kum kia kro.")

while True:
    print("===== Menu =======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if( choice == 1 ):

        date = input("Enter Date of Expense: ")
        category = input("Enter Category of Expense (Food, Travel, Books): ")
        description = input("Enter Description of Expense: ")
        amount = float(input("Enter Amount of Expense: "))

        expenses = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expenses)
        print("\nExpenses added Successfully")

        # 2 View All Expenses

    elif(choice==2):
            if (len(expensesList)==0):
                print("Expenses are empty")
            else:
                print("===== This is Your Expenses =====")
                count = 1
                for eachExpense in expensesList:
                    print(f"{count} -> {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']}, {eachExpense['amount']}")
                    count += 1

        # 3 View Total Expenses
    elif(choice==3):
            total = 0
            for eachExpense in expensesList:
                total += eachExpense['amount']
            print("\n Total Expense: ", total)

        # 4 Exit
    elif(choice==4):
        print("Thank you for using Expense Tracker")
        break
    else:
        print("Invalid Choice. Try again")