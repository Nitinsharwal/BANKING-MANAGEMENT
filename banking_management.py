database = {}
def add_record(username, pin):
    if username in database:
        print("User already exists.\n")

    else:
        database[username] = {'pin':pin, 'balance':0}
        print("\nUser added successfully.\n")
        choices(username)

def view_records():
    if database:
        for username, pin in database.items():
            key = input('Enter user name : ')
            if key == username:
                print(f"\nUSERNAME : {username}, PIN & BALANCE : {pin}")
            else:
                print('\nPlease enter correct username to get pin..!\n')
            break
    else:
        print("\nDatabase is empty.")

def choices(username):
    choice = input('A. DEPOSIT \nB. WITHDRAW \nC. CHECK BALANCE \nD. QUIT \nWhat you want : ').capitalize()
    if(choice=='A'):
        deposit(username)
    elif(choice=='B'):
        withdraw(username)
    elif(choice=='C'):
        check_Balance(username)
    elif(choice=='D'):
        print('EXITING...THANKS FOR VISITING..!')
        exit()
    else:
        print('Invaild choice!')


def deposit(username):
    money = int(input('\nHow much money you want to deposit : '))
    database[username]['balance']+=money
    print(f'\n{money} has been deposited in {username} account\n')
    choices(username)

def withdraw(username):
    with_money = int(input('\nHow much money you want to withdraw : '))
    if with_money <= database[username]['balance']:
        database[username]['balance']-=with_money
        print(f'\nCurrent balance of {username} : {database[username]['balance']}')
        
    else:
        print('\nInsufficient balance\n')
    choices(username)

def check_Balance(username):
    print(f'\nCurrent balance of {username} : {database[username]['balance']}')
    choices(username)

    

while True:
    print("\n---USERS MENU----  \n1. Add user \n2. View user \n3.Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input('Enter user name : ')
        pin = input('Enter 4 digit PIN : ')
        add_record(username=username,pin=pin)

    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Exiting...!")
        break
    else:
        print("Invalid choice. Please try again.")
