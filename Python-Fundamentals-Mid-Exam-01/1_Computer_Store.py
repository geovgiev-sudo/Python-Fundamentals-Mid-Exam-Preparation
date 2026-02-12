vanilla_price = 0
vanilla_price_tax = 0
total_tax = 0
total_price = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print(f"Invalid price!")
        continue
    tax = price * 0.20
    total_tax += tax
    price_tax = price + tax
    vanilla_price += price
    vanilla_price_tax += price_tax

if vanilla_price_tax == 0:
    print(f"Invalid order!")
    exit()

if command == "special":
    total_price = vanilla_price_tax - vanilla_price_tax * 0.10

elif command == "regular":
    total_price = vanilla_price_tax

print(f"Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {vanilla_price:.2f}$\n"
      f"Taxes: {total_tax:.2f}$\n"
      f"-----------\n"
      f"Total price: {total_price:.2f}$")