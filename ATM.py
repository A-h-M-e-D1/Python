print("---------------------- Welcome to Bank Account ------------------------")

class Login:
    def __init__(self, ID, PIN):
        self.ID = ID
        self.PIN = PIN 
user_id = int(input("Enter The ID: "))
user_PIN = int(input("Enter The PIN: "))

class PersonalInformation:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def show_info(self):
        return f"Name is: {self.name}\nAge is: {self.age}\nCity is: {self.city}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_address = input("Enter your City: ")

class Op_on_Bankaccount(PersonalInformation):

    def __init__(self, name, age, city, balance):
        super().__init__(name, age, city)
        self.balance = balance

    def choose_operation(self):
        print("What operation do you want to perform:")
        print("1-Deposit")
        print("2-Withdraw")
        print("3-Finish operation")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")

user_balance = float(input("Enter Your Balance: "))
user_info = Op_on_Bankaccount(user_name, user_age, user_address, user_balance)

while True:
    user_info.choose_operation()
    user_input = int(input())
    
    if user_input == 1:
        deposit_amount = float(input("Enter the amount to deposit: "))
        user_info.deposit(deposit_amount)
        print(f"New balance: {user_info.balance}")
    elif user_input == 2:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        user_info.withdraw(withdraw_amount)
        print(f"New balance: {user_info.balance}")
    elif user_input == 3:
        print(f"You finished process and total baalnce is {user_info.balance}$")
        break
    else:
        print("Invalid choice. Please select 1 for Deposit or 2 for Withdraw.")
