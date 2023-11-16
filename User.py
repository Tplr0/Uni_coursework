import __main__


def usermenu():
    while True:
        print(" ")
        print("User Menu")
        print("---------------")
        print("1) Login with account")
        print("2) Sign up as new user")
        print("3) Exit to main menu")
        print("4) Exit program")
        choice = input("Enter your choice: ")
        if choice == "1":
            userlogin()
            # print("Coming soon")
        elif choice == "2":
            usersignup()
            # print("coming soon")
        elif choice == "3":
            __main__.mainmenu()
            pass
        elif choice == "4":
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            usermenu()


def userlogin():
    while True:
        print(" ")
        print("User Login")
        print("-----------------")
        inputun = input("Enter your username:")
        inputpwd = input("Enter your password:")

        file = open("userlogin.txt")
        data = file.read()

        if inputun in data and inputpwd in data:
            userhallmenu()
        else:
            print("Invalid login!")
            usermenu()


def usersignup():
    while True:
        inputun = input("Enter your desired username:")
        inputpwd = input("Enter your desired password:")

        f = open("userlogin.txt", "a")
        f.write(inputun + " " + inputpwd)
        f.write("\n")

        f.close()
        print("Thank you for signing up!")
        print("Redirecting you to user login ..... ")
        userlogin()


def userhallmenu():
    while True:
        print(" ")
        print("User Hall Menu")
        print("----------------")
        print("1) Enter Hall Information")
        print("2) View all the hall information")
        print("3) Search the hall information")
        print("4) Go back to main menu")
        print("5) Back to user menu")
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
            usermenu()
        elif choice == '6':
            print("System exited")
            exit()
        else:
            print("Invalid!")
