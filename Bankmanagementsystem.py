
users = {}
balance = 0 
is_running = True

def register():
    username = input("Create a username: ")
    if username in users:
        print("Username already exists. Please choose another.")
        return False

    password = input("Create a password: ")
    user_id = input("Enter your ID: ")

    users[username] = {'id': user_id, 'password': password}
    print("Registration successful!")
    return True

def login():
    print("Welcome to the Bank Management System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]['password'] == password:
        print(f"Login successful! Welcome, {username}.")
        return username  # Return the username upon successful login
    else:
        print("Invalid username or password.")
        return None

def showbalancecit():
    print(f"Your balance is: ${balance}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))
    if amount <= 0:
        print("Your amount is invalid.")
        return 0
    else:
        print(f"You have successfully deposited: ${amount}")
        return amount

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount <= 0:
        print("Your amount must be greater than zero.")
        return 0
    else:
        print(f"You have successfully withdrawn: ${amount}")
        return amount

# Main program loop
while True:
    print("*******************************************************************************")
    print("*                    Bank Management System                                   *")
    print("*******************************************************************************")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        username = login()
        if username:  
            is_running = True
            while is_running:
                print("\nBank Management System")
                print("1. Show Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                choice = input("Enter the number from 1 to 4: ")

                if choice == '1':
                    showbalancecit()
                elif choice == '2':
                    balance += deposit()
                elif choice == '3':
                    balance -= withdraw()
                elif choice == '4':
                    is_running = False
                else:
                    print("Sorry! You chose a wrong number.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")

print("Thank you. See you again!")