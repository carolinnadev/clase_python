from funciones_14 import get_option, check_password, withdrawal_menu, subtract, get_number, add, update_password


balance = [500000]
current_password = [9863]


while True:

    print("""Menu
    1. Check balance
    2. Withdraw money
    3. Deposit money
    4. Change password
    5. Exit the system""")

    menu = get_option()
    print("=" * 70)

    match menu:

        case 1:
            if check_password(current_password):
                print("Your balance is:", balance)
                print("=" * 70)

        case 2:
            if check_password(current_password):

                while True:

                    sub_menu = withdrawal_menu()

                    match sub_menu:

                        case 1:
                            a = balance[0]
                            b = "20000"
                            saldo_actual = subtract(a, b)
                            balance.clear()
                            balance.append(saldo_actual)
                            print("Your current balance is:", balance)
                            print("=" * 70)

                        case 2:
                            a = balance[0]
                            b = "50000"
                            saldo_actual = subtract(a, b)
                            balance.clear()
                            balance.append(saldo_actual)
                            print("Your current balance is:", balance)
                            print("=" * 70)

                        case 3:
                            a = balance[0]
                            b = "100000"
                            saldo_actual = subtract(a, b)
                            balance.clear()
                            balance.append(saldo_actual)
                            print("Your current balance is:", balance)
                            print("=" * 70)

                        case 4:
                            a = balance[0]
                            b = "200000"
                            saldo_actual = subtract(a, b)
                            balance.clear()
                            balance.append(saldo_actual)
                            print("Your current balance is:", balance)
                            print("=" * 70)

                        case 5:
                            print("=" * 70)
                            a = balance[0]
                            b = get_number()
                            saldo_actual = subtract(a, b)
                            balance.clear()
                            balance.append(saldo_actual)
                            print("Your current balance is:", balance)
                            print("=" * 70)

                        case 6:
                            print("Returning to the previous menu...")
                            print("=" * 70)
                            break

        case 3:
            if check_password(current_password):

                a = balance[0]
                b = get_number()
                saldo_actual = add(a, b)

                balance.clear()
                balance.append(saldo_actual)

                print("Your current balance is:", balance)
                print("=" * 70)

        case 4:
            if check_password(current_password):
                update_password(current_password)

        case 5:
            print("Exiting the system")
            break