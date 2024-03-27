class User:
    def __init__(self, name, roll_number, email, password):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.password = password

class RegisterPage:
    def __init__(self):
        self.users = {}

    def register_user(self, user):
        self.users[user.roll_number] = user

    def is_roll_number_registered(self, roll_number):
        return roll_number in self.users

    def get_user_by_roll_number(self, roll_number):
        return self.users.get(roll_number)

class LoginPage:
    def __init__(self, register_page):
        self.register_page = register_page
        self.logged_in_user = None

    def login(self, roll_number, password):
        if not self.register_page.is_roll_number_registered(roll_number):
            print("User not registered.")
        else:
            user = self.register_page.get_user_by_roll_number(roll_number)
            if user.password == password:
                self.logged_in_user = user
                print("Login successful.")
            else:
                print("Password incorrect.")

    def display_profile(self):
        if self.logged_in_user:
            print("Name:", self.logged_in_user.name)
            print("Roll Number:", self.logged_in_user.roll_number)
            print("Email:", self.logged_in_user.email)
        else:
            print("No user logged in.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out.")

register_page = RegisterPage()
login_page = LoginPage(register_page)

while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Display Profile")
    print("4. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        roll_number = input("Enter your roll number: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        new_user = User(name, roll_number, email, password)
        register_page.register_user(new_user)
        print("User registered successfully.")

    elif choice == "2":
        roll_number = input("Enter your roll number: ")
        password = input("Enter your password: ")
        login_page.login(roll_number, password)

    elif choice == "3":
        login_page.display_profile()

    elif choice == "4":
        login_page.logout()

    else:
        print("Invalid choice. Please choose again.")
