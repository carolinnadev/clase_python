import time


def check_password(current_password):

    intentos = 3

    while True:

        for intento in range(intentos):

            password = int(input("Enter the password: "))

            if not password:
                print("Error: you may only enter numbers.")
                continue

            if password == current_password[0]:
                print("Access granted")
                print("=" * 70)
                return True

            print("Incorrect password.")
            print("Attempts remaining:", intentos - intento - 1)

        else:

            print("\nYou have used all 3 attempts.")
            print("Wait 1 minute before trying again.")

            for segundos in range(60, 0, -1):
                print(
                    f"\rYou can try again in {segundos} seconds...",
                    end=""
                )
                time.sleep(1)

            print("\n")


def get_option():

    while True:

        try:
            num1 = int(input("Enter a option: "))
            return num1

        except ValueError:
            print("Enter a valid number")


def get_number():

    while True:

        try:
            number = int(input("Enter a number: "))
            return number

        except ValueError:
            print("Error: you must enter valid numbers, try again")


def withdrawal_menu():

    print("\nHow much would you like to withdraw?")
    print("1. 20000")
    print("2. 50000")
    print("3. 100000")
    print("4. 200000")
    print("5. Enter a different amount")
    print("6. Return to the main menu")

    option = get_option()

    return option


def subtract(first_number, second_number):
    return int(first_number) - int(second_number)


def add(first_number, second_number):
    return int(first_number) + int(second_number)


def update_password(current_password):

    while True:

        password1 = int(input("Enter the new password: "))
        password2 = int(input("Enter the password again: "))

        if password1 < 1000 or password1 > 9999:
            print("The password must have 4 digits")
            continue

        if password2 < 1000 or password2 > 9999:
            print("The password must have 4 digits")
            continue

        if password1 == password2:

            if password1 != current_password[0]:

                current_password.clear()
                current_password.append(password1)

                print("You changed the password.")
                break

            else:
                print("You cannot enter the previous password")

        else:

            print("The passwords do not match")