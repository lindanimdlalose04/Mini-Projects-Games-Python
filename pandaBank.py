import random
import json
import os


accounts = {
    1234567: {"name": "Alice", "surname": "Smith", "balance": 50000.0, "account": 1234567},
    2345678: {"name": "Bob", "surname": "Johnson", "balance": 3000.0, "account": 2345678},
    3456789: {"name": "Charlie", "surname": "Brown", "balance": 170000.0, "account": 3456789},
}


def deposit_money():
    print("********")
    print("To deposit money enter the following details.")
    name = input("Enter the client's name: ")
    try:
        accountNumber = int(input("Enter the account number: "))
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("❌ Invalid input. Numbers only.")
        return

    if accountNumber in accounts and accounts[accountNumber]['name'] == name:
        accounts[accountNumber]['balance'] += amount
        print("✅ New balance:", accounts[accountNumber]['balance'])
    else:
        print("❌ Account not found. Try again")

    choice = input("\nWould you like to continue banking? (y/n): ").lower()
    if choice == "n":
        main_menu()


def withdraw_money():
    print("To withdraw money enter the following details.")
    name = input("Enter the client's name: ")
    try:
        accountNumber = int(input("Enter the account number: "))
        withdraw_amount = float(input("Enter the amount to withdraw: "))
    except ValueError:
        print("❌ Invalid input. Numbers only.")
        return

    if accountNumber in accounts and accounts[accountNumber]['name'] == name:
        print("Your current balance is:", accounts[accountNumber]['balance'])
        if withdraw_amount <= accounts[accountNumber]['balance']:
            accounts[accountNumber]['balance'] -= withdraw_amount
            print("✅ New balance:", accounts[accountNumber]['balance'])
        else:
            print("❌ You cannot withdraw more than your balance.")
    else:
        print("❌ Account not found. Try again")

    choice = input("\nWould you like to continue banking? (y/n): ").lower()
    if choice == "n":
        main_menu()


def transfer_money():
    print("*************")
    print("To transfer money enter the following details.")
    name = input("Enter the client's name: ")
    try:
        from_account = int(input("Enter the account number transferring from: "))
    except ValueError:
        print("❌ Invalid input. Numbers only.")
        return

    if from_account in accounts and accounts[from_account]['name'] == name:
        try:
            to_account = int(input("Enter recipient account number: "))
            amount = float(input("Enter amount to transfer: "))
        except ValueError:
            print("❌ Invalid input. Numbers only.")
            return

        if to_account in accounts:
            if amount <= accounts[from_account]['balance']:
                accounts[from_account]['balance'] -= amount
                accounts[to_account]['balance'] += amount
                print("✅ Transfer successful! Your new balance:", accounts[from_account]['balance'])
                print(accounts[to_account]['name'], "now has:", accounts[to_account]['balance'])
            else:
                print("❌ Insufficient balance.")
        else:
            print("❌ Recipient account not found.")
    else:
        print("❌ Your account details are incorrect.")

    choice = input("\nWould you like to continue banking? (y/n): ").lower()
    if choice == "n":
        main_menu()


def check_balance():
    print("******")
    print("To check balance enter the following details.")
    name = input("Enter the client's name: ")
    try:
        accountNumber = int(input("Enter the account number: "))
    except ValueError:
        print("❌ Invalid input. Numbers only.")
        return

    if accountNumber in accounts and accounts[accountNumber]['name'] == name:
        print("✅ Current balance:", accounts[accountNumber]['balance'])
    else:
        print("❌ Account not found.")

    choice = input("\nWould you like to continue banking? (y/n): ").lower()
    if choice == "n":
        main_menu()


def save(accounts):
    filepath = input("📂 Enter file path to save accounts (e.g., accounts.json): ")
    if not filepath.endswith(".json"):
        print("❌ Invalid file format. Please use a .json extension.")
        return
    try:
        with open(filepath, "w") as f:
            json.dump(accounts, f, indent=4)
        print(f"✅ Accounts saved successfully to {filepath}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")


def load():
    filepath = input("📂 Enter file path to load accounts (e.g., accounts.json): ")
    if not os.path.exists(filepath):
        print("❌ File not found.")
        return None
    if not filepath.endswith(".json"):
        print("❌ Wrong format. Only .json files are allowed.")
        return None
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("❌ Invalid file format.")
            return None
        print(f"✅ Accounts loaded successfully from {filepath}")
        return data
    except json.JSONDecodeError:
        print("❌ Error: File is not valid JSON.")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
    return None


def create_account():
    print("**********")
    name = input("Enter first name: ")
    surname = input("Enter surname: ")
    try:
        balance = float(input("Enter opening balance: "))
    except ValueError:
        print("❌ Invalid input. Balance must be a number.")
        return

    accountNumber = random.randint(1000000, 9999999)
    accounts[accountNumber] = {
        "name": name,
        "surname": surname,
        "balance": balance,
        "account": accountNumber
    }
    print("\n✅ Account created. Account number:", accountNumber)

    choice = input("\nWould you like to continue banking with this account? (y/n): ").lower()
    if choice == "n":
        return


def menuexisting():
    while True:
        print("\n====== EXISTING CLIENT MENU ======")
        print("1. Deposit funds")
        print("2. Withdraw funds")
        print("3. Transfer funds")
        print("4. Check balance")
        print("5. Save accounts to file")
        print("6. Load accounts from file")
        print("7. EXIT to main menu")

        choice = input("\nSelect an option (1-7): ")

        if choice == "1":
            deposit_money()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            transfer_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            save(accounts)
        elif choice == "6":
            loaded = load()
            if loaded is not None:
                accounts.update(loaded)
        elif choice == "7":
            print("Exiting to main menu...")
            break
        else:
            print("❌ Invalid option. Try again.")


def main_menu():
    while True:
        print("\n=================================")
        print("WELCOME TO PANDA BANK SYSTEM (Admin Console)")
        print("=================================")
        print("1. Register a New Account")
        print("2. Manage Existing Accounts")
        print("3. Exit System")

        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            menuexisting()
        elif choice == "3":
            print("Closing system...")
            break
        else:
            print("❌ Invalid choice. Try again.")


main_menu()
