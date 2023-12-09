import time
import os

# Clear the screen
def clearDisplay():
    os.system('cls' if os.name == 'nt' else 'clear')

# Simulate a loading screen
def loadingScreen():
    print("Processing", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="")
    print("\n")

# Check if an account number exists
def checkAccount(account_number, account_list):
    for account in account_list:
        if account_number == account[0]:
            return True
    return False

# Create a new account
def newAccount(account_list):
    account_number = input('Enter account No.:')
    if checkAccount(account_number, account_list):
        print('This number is already in the system')
        return False
    customer_name = input('Enter customer name:')
    mobile_number = input('Enter customer mobile:')
    account_list.append([account_number, customer_name, mobile_number])
    return True

# Process a deposit
def makeDeposit(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not checkAccount(account_number, account_list):
        print('There is no account with this number')
        return False
    amount = input('Enter the amount to be deposited:')
    transaction_list.append([account_number, 'd', amount])
    return True

# Process a withdrawal
def makeWithdrawal(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not checkAccount(account_number, account_list):
        print('There is no account with this number')
        return False
    amount = input('Enter the amount to be withdrawn:')
    balance = calculateBalance(account_number, transaction_list)
    if float(amount) > balance:
        print('No sufficient fund')
        return False
    transaction_list.append([account_number, 'w', amount])
    return True

# Display account information
def accountInquiry(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not checkAccount(account_number, account_list):
        print('There is no account with this number')
        return False
    for account in account_list:
        if account[0] == account_number:
            print('Name: ' + account[1])
            print('Mobile: ' + account[2])
            print('Balance: ' + str(calculateBalance(account_number, transaction_list)))
            break
    return True

# Calculate the balance of an account
def calculateBalance(account_number, transaction_list):
    deposit_total = 0
    withdrawal_total = 0
    for transaction in transaction_list:
        if transaction[0] == account_number:
            if transaction[1] == 'd':
                deposit_total += float(transaction[2])
            elif transaction[1] == 'w':
                withdrawal_total += float(transaction[2])
    return deposit_total - withdrawal_total

# Load accounts data
def loadAccountData(filepath):
    account_list = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if line.strip():
                    account_list.append(line.strip().split(','))
        return account_list
    except FileNotFoundError:
        print("No such file: '" + filepath + "'")
        return []

# Load transactions data
def loadTransactionData(filepath):
    transaction_list = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if line.strip():
                    transaction_list.append(line.strip().split(','))
        return transaction_list
    except FileNotFoundError:
        print("No such file: '" + filepath + "'")
        return []

# Display the main menu
def showMainMenu():
    clearDisplay()
    print("***************************************")
    print("*          BANKING SYSTEM             *")
    print("***************************************")
    print("* 1- Open a new account               *")
    print("* 2- Deposit                          *")
    print("* 3- Withdraw                         *")
    print("* 4- Inquiry                          *")
    print("* 5- Exit                             *")
    print("***************************************")
    user_choice = input("Your choice: ")
    loadingScreen()
    return user_choice

def runBankingSystem():
    accounts = loadAccountData('accounts.txt')
    transactions = loadTransactionData('transactions.txt')

    while True:
        choice = showMainMenu()
        if choice == '1':
            newAccount(accounts)
        elif choice == '2':
            makeDeposit(accounts, transactions)
        elif choice == '3':
            makeWithdrawal(accounts, transactions)
        elif choice == '4':
            accountInquiry(accounts, transactions)
        elif choice == '5':
            print('Exiting the system. Goodbye!')
            loadingScreen()
            break
        else:
            print('Invalid choice, please try again.')
            time.sleep(2)

runBankingSystem()
