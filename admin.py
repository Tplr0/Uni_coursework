import __main__


def login():
    while True:
        print(" ")
        print("Admin Login")
        print("-----------------")
        inputun = input("Enter your username:")
        inputpwd = input("Enter your password:")
        file = open("adminlogin.txt")
        data = file.read()

        if inputun in data and inputpwd in data:
            admin_menu()
        else:
            print("Invalid login!")
            login()


def admin_menu():
    while True:
        print(" ")
        print("Admin Menu")
        print("----------------")
        print("1) Enter Hall Information")
        print("2) View all the hall information")
        print("3) Search the hall information")
        print("4) Go back to main menu")
        print("5) Back to admin login")
        print("6) Exit program")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Coming Soon")
            pass
        elif choice == '2':
            print("Coming Soon")
            pass
        elif choice == '3':
            print("Coming Soon")
            pass
        elif choice == '4':
            __main__.mainmenu()
            pass
        elif choice == '5':
            login()
        elif choice == '6':
            print("System exited")
            exit()
        else:
            print("Invalid!")
            admin_menu()
