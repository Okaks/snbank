import random
import string
import os


def bank_customer_details():
    with open("customer.txt") as user_details:
    if os.path.getsize("customer.txt") != 0:
        Customer_Details = bank_customer_details.load(user_details)
    else:
        Customer_Details = {}
        Customer_Details["account"] = []

    def create_session(staff, action=None):
        with open(f"{staff.username}.txt") as session:
            session.write(f"{staff.username} {action} \n")

    def User(staff):
        User.username = None
        User.password = None
        User.logged_in = False

    def start(staff):
        print("""
        1 Staff Login
        2 Close App
        """)
        response = ""
        while response == "" or response > 2:
            response = int(input("> "))
        else:
            if response == 1:
                staff.login_details()
            else:
                staff.close_app()

    def login(staff):
        while not staff.logged_in:
            print("wrong info, please enter correct details")
            username = input("Enter username: ").upper()
            password = input("Enter password: ")
            with open("staff.txt", "r") as staff.txt:
                for user in staff["data"]:
                    if username == user["username"].lower() and password == user["password"]:
                        staff.username = username
                        staff.password = password
                        staff.logged_in = True
                        break
                    else:
                        staff.logged_in = False
        else:
            staff.create_session(action="log in successful")
            staff.show_account_options()

    def show_account_options(staff):
        print("""
        1 Create new bank account
        2 Check Account Details
        3 Logout
        """)
        response = ""
        while response == "" or response > 3:
            response = int(input("> "))
        else:
            if response == 1:
                staff.create_account()
            elif response == 2:
                staff.get_account_details()
            else:
                staff.logout()

    def create_account(staff):
        details = {}
        details["Account name"] = input("Account name: ")
        try:
            details["Opening balance"] = int(input("Opening balance: "))
        except:
            raise TypeError("Must be an integer")
        details["Account type"] = input("Account type: ")
        details["Account email"] = input("Account email: ")
        details["Account number"] = "".join(random.choice(string.digits) for i in range(10))
        print(f"The account number is {details['Account number']}")
        bank_customer_details.append(details)
        with open("customer.txt") as user_details:

        staff.create_session(action=f"created account{details['Account name']}")
        staff.show_account_settings()

    def logout(staff):
        os.remove(f"{staff.username}.txt")
        staff.username, staff._password, staff.logged_in = None, None, False
        staff.start()
        return logout

    def get_account_details(staff):
        account_number = input("Account number: ")
        with open("customer.txt", "r") as customer:
            total_details = bank_customer_details.load(customer)
            for data in total_details["account"]:
                if account_number == data["Account number"]:
                    user_details = data
                    break
        for key, values in user_details.items():
            print(f"\t\t{key}, {values}")
        staff._show_account_settings()
        return get_account_details


    def close_app():
        return close_app
