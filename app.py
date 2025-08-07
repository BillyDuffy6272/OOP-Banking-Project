from account import Account
from account_wd import Account_wd
from account_storage import Account_storage
from account_login import Account_Login
import csv
# Import information, variables, and classes from other files

what_to_do = input("Do you want to login or create an account? (login/create): ")

def creating_account():
    global name, account_number, account_balance
    # Create a new account
    account = Account()
    account_name_input = input("What is the account name : ")
    while True:
        # Allows the user to input a valid account number, with error handling for length
        account_number_input = input("Please enter a unqiue 8-digit account number: ")
        if len(account_number_input) == 8:
            print("You have entered a valid account number")
        elif len(account_number_input) < 8:
            print("idiot, you have entered too less than 8")
            continue
        else:
            print("idiot, you have entered too more than 8")
            continue
        break
    while True:
        try:
            account_balance_input = int(input("How rich are you (initial balance)? "))
        except:
            print("Ensure it is a valid number, try again")
        else:
            break
    print(" ")
    print(" ")
    print(" ")
    # Sign up the account with the provided details
    account.signup(account_name_input, account_number_input, account_balance_input)
    # Display the account information
    account.display_info()
    print(" ")
    print(" ")
    print(" ")

    # Store the account information in a CSV file
    storage = Account_storage(account_name_input, account_number_input, account_balance_input)
    storage.account_store()

    # Set the user input into shorter variables for later use
    name = account_name_input
    account_number = account_number_input
    account_balance = account_balance_input

def update_account_info(name, account_number, account_balance):
    # Update the account information in the CSV file, used mostly in deposit and withdraw
    updated_rows = []
    with open("account_info.csv", mode="r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == name and row[1] == account_number:
                updated_rows.append([name, account_number, account_balance])
            else:
                updated_rows.append(row)

    with open("account_info.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(updated_rows)
    

if what_to_do.lower() == "create":
    creating_account() # Create a new account

    store = Account_wd(name, account_number, account_balance) # Create an instance of Account_wd for deposit and withdraw
    account_balance = store.d_w() # Update the account balance after deposit or withdraw

    update_account_info(name, account_number, account_balance) # Update the account information in the CSV file
elif what_to_do.lower() == "login":
    login = Account_Login(None, None, None) # Login to an existing account
    account_login = login.login() # Runs the login function
    if account_login:
        name, account_number, account_balance = account_login
        store = Account_wd(name, account_number, account_balance) 
        account_balance = store.d_w()
        update_account_info(name, account_number, account_balance)

        display = Account_wd(name, account_number, account_balance)
        print(" ")
        print(" ")
        print(" ")
        display_info = display.display_info()
    else:
        print("Login failed. Please restart the program.")
        exit()

    store = Account_wd(name, account_number, account_balance)
    account_balance = store.d_w()

    update_account_info(name, account_number, account_balance)
else:
    print("Invalid option. Please restart the program")





