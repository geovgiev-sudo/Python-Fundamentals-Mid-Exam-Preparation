energy = int(input())
command = input()
battles_won = 0

while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        battles_won += 1
    else:
        print(f"Not enough energy! Game ends with {battles_won} "
              f"won battles and {energy} energy")
        break
    if battles_won % 3 == 0:
        energy += battles_won

    command = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")