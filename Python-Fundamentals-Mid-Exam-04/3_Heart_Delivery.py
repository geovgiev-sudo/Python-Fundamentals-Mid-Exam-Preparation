neighborhood = list(map(int, input().split("@")))
command = input()
current_house = 0
while command != "Love!":
    command = command.split()
    step = int(command[1])
    current_house += step
    if current_house >= len(neighborhood):
        current_house = 0

    if neighborhood[current_house] > 0:
        neighborhood[current_house] -= 2
        if neighborhood[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")

    elif neighborhood[current_house] <= 0:
        print(f"Place {current_house} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_house}.")
if sum(neighborhood) == 0:
    print(f"Mission was successful.")
else:
    failed_places = 0
    for i in neighborhood:
        if i != 0:
            failed_places += 1
    print(f"Cupid has failed {failed_places} places.")
