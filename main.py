import admin
import User
# import admin and user to direct the user to admin or user login


def mainmenu():
    while True:
        print(" ")
        print("Main Menu:")
        print("-------------------")
        print("1) Login as Admin")
        print("2) Login as User")
        print("3) Exit Program")
        choice = input("Enter your choice: ")
        # User is directed to admin login if they input 1 or user if they input 2
        if choice == '1':
            admin.login()
        elif choice == '2':
            User.usermenu()
        elif choice == '3':
            print("System exited")
            exit()  # User is exited from the system
        else:
            print("Invalid Choice!")
            print(" ")
            mainmenu()

    # start the program


mainmenu()
