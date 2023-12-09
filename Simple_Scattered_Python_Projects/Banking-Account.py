# Function to display the main menu and handle the user's choice
def showMainMenu():
    print("Please select one of the following:")
    print("1- Open a new account")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- Inquiry")
    print("5- Exit")
    return input("Your choice:")

# Function to check if an account number exists
def doesAccountExist(account_number, account_list):
    for account in account_list:
        if account_number == account[0]:
            return True
    return False

# Function to create a new account
def addNewAccount(account_list):
    account_number = input('Enter account No.:')
    if doesAccountExist(account_number, account_list):
        print('This number is already in the system')
        return False
    customer_name = input('Enter customer name:')
    mobile_number = input('Enter customer mobile:')
    account_list.append([account_number, customer_name, mobile_number])
    return True

# Function to process a deposit
def processDeposit(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not doesAccountExist(account_number, account_list):
        print('There is no account with this number')
        return False
    amount = input('Enter the amount to be deposited:')
    transaction_list.append([account_number, 'd', amount])
    return True

# Function to process a withdrawal
def processWithdrawal(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not doesAccountExist(account_number, account_list):
        print('There is no account with this number')
        return False
    amount = input('Enter the amount to be withdrawn:')
    balance = calculateAccountBalance(account_number, transaction_list)
    if float(amount) > balance:
        print('No sufficient fund')
        return False
    transaction_list.append([account_number, 'w', amount])
    return True

# Function to display account information
def accountEnquiry(account_list, transaction_list):
    account_number = input('Enter account No.:')
    if not doesAccountExist(account_number, account_list):
        print('There is no account with this number')
        return False
    for account in account_list:
        if account[0] == account_number:
            print('Name: ' + account[1])
            print('Mobile: ' + account[2])
            print('Balance: ' + str(calculateAccountBalance(account_number, transaction_list)))
            break
    return True

# Function to calculate the balance of an account
def calculateAccountBalance(account_number, transaction_list):
    deposit_sum = 0.0
    withdraw_sum = 0.0
    for transaction in transaction_list:
        if transaction[0] == account_number:
            if transaction[1] == 'd':
                deposit_sum += float(transaction[2])
            elif transaction[1] == 'w':
                withdraw_sum += float(transaction[2])
    return deposit_sum - withdraw_sum

# Function to load data from accounts file
def readAccountsData(file_path):
    accounts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    accounts.append(line.strip().split(','))
        return accounts
    except FileNotFoundError:
        print("No such file: '" + file_path + "'")
        return []

# Function to load data from transactions file
def readTransactionsData(file_path):
    transactions = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    transactions.append(line.strip().split(','))
        return transactions
    except FileNotFoundError:
        print("No such file: '" + file_path + "'")
        return []

# Main function to run the banking system
def runBankingSystem():
    accounts_file = 'accounts.txt'
    transactions_file = 'transactions.txt'

    # Load the accounts and transactions data from the files
    accounts = readAccountsData(accounts_file)
    transactions = readTransactionsData(transactions_file)

    while True:
        choice = showMainMenu()

        if choice == '1':
            addNewAccount(accounts)
        elif choice == '2':
            processDeposit(accounts, transactions)
        elif choice == '3':
            processWithdrawal(accounts, transactions)
        elif choice == '4':
            accountEnquiry(accounts, transactions)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

# Uncomment the line below to run the program in a local environment
runBankingSystem()
