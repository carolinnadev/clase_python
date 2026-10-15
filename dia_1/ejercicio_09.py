from funciones_09 import get_price

HEADER = '\033[38;2;0;200;255m'
OKBLUE = '\033[38;2;255;193;7m'
OKCYAN = '\033[38;2;255;224;160m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

price=get_price()

print(HEADER + '''For purchases iguales o superiores a 200.000, you get a 20% discount.
For purchases iguales o superiores a 100.000, you get a 10% discount.
Por compras inferiores a 100.000 no obtienes ningun descuento en el momento.''' + ENDC)
print()

first_discount=200000
second_discount=100000

if price >= first_discount:
    print(OKCYAN + "We will deduct 20% from the value of your purchase." + ENDC)
    print()
    total=price-((price*20)/100)
    print(OKBLUE + f"the total value of your purchase is {total} pesos" + ENDC)

elif price >= second_discount:
    print(OKCYAN + "We will deduct 10% from the value of your purchase." + ENDC)
    print()
    total=price-((price*10)/100)
    print(OKBLUE + f"the total value of your purchase is {total} pesos" + ENDC)

else:
    print(OKCYAN + f'''Remember that for purchases iguales o superiores a {first_discount}, you will receive a 20% discount.
    Remember that for purchases iguales o superiores a {second_discount}, you will receive a 10% discount. ''')
    print(OKBLUE + f"Your amount to pay is {price} pesos" + ENDC)