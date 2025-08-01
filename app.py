from account import Account

def creating_account():
    account = Account()
    account_name_input = input("What is the account name : ")
    while True:
        account_number_input = input("Please enter a unqiue 8-digit account number: ")
        if len(account_number_input) == 8:
            print("Wellest done, youdif entered 8 values")
        elif len(account_number_input) < 8:
            print("Blimey idiot, youdve entered too less thanif 8")
            continue
        else:
            print("Blimey idiot, youdve entered too more thanif 8")
            continue
        break
    while True:
        try:
            account_balance_input = int(input("How rich are you (initial balance)? "))
        except:
            print("Wouldve thou ensure it is thy valid number")
        else:
            break
    account.signup(account_name_input, account_number_input, account_balance_input)
    account.display_info()

creating_account()