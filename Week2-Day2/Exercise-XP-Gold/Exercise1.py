# PART I 
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"{self.username} has been authenticated successfully.")
        else:
            raise Exception("Invalid username or password.")
    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")

# PART II 
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Minimum balance of {self.minimum_balance} must remain.")
        self.balance -= amount
        print(f"{amount} withdrawn. Remaining balance: {self.balance}")

# PART IV 
class ATM:
    def __init__(self, account_list, try_limit=2):
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must contain only BankAccount or MinimumBalanceAccount instances.")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit provided. Defaulting to 2.")
            try_limit = 2
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()
    def show_main_menu(self):
        while True:
            print("\n=== ATM MAIN MENU ===")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Try again.")
    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print(f"Welcome, {username}!")
                self.show_account_menu(account)
                return
            except Exception:
                continue  
        self.current_tries += 1
        print(f"Invalid credentials. Attempts: {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down ATM.")
            exit()
    def show_account_menu(self, account):
        while True:
            print(f"\n=== {account.username}'s Account Menu ===")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print(e)
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(e)
            elif choice == "3":
                print(f"Logging out {account.username}.")
                account.authenticated = False
                break
            else:
                print("Invalid choice. Try again.")
