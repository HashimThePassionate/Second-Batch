class Account:
    def __init__(self, account_number: int, pin: int, balance : int=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self)-> int:
        return self.balance

    def deposit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def __str__(self) -> str:
        return f" New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

class Card:
    def __init__(self, card_number :int, account : Account ):
        self.card_number = card_number
        self.account = account

class ATM:
    def __init__(self):
        self.card_inserted:bool = False
        self.current_card = None

    def insert_card(self, card: Card) -> str:
        self.card_inserted :bool = True
        self.current_card = card
        return "Card inserted. Please enter your PIN."

    def eject_card(self):
        self.card_inserted = False
        self.current_card = None
        return "Card ejected. Thank you."

    def authenticate(self, pin):
        if self.card_inserted and self.current_card and self.current_card.ccount.pin == pin:
            return True
        else:
            return False

    def check_balance(self):
        if self.authenticate(input("Enter your PIN: ")):
            return f"Your balance is ${self.current_card.account.check_balance()}"
        else:
            return "Authentication failed."

    def deposit(self, amount):
        if self.authenticate(input("Enter your PIN: ")):
            return self.current_card.account.deposit(amount)
        else:
            return "Authentication failed."

    def withdraw(self, amount):
        if self.authenticate(input("Enter your PIN: ")):
            return self.current_card.account.withdraw(amount)
        else:
            return "Authentication failed."

# Example usage:
account1 = Account(account_number="123456789", pin="1234", balance=1000)
card1 = Card(card_number="1111222233334444", account=account1)
atm_machine = ATM()

print(atm_machine.insert_card(card1))
print(atm_machine.check_balance())  # Authenticate with PIN
print(atm_machine.deposit(200))     # Authenticate with PIN
print(atm_machine.withdraw(50))     # Authenticate with PIN
print(atm_machine.eject_card())
