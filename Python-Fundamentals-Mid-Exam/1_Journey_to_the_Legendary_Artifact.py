energy = float(input())
command = input()
moves = 0
pieces_found = 0
while command != "Journey ends here!":

    if command == "mountain":
        energy -= 10
        moves += 1
        if moves % 3 == 0:
            pieces_found += 1
            if pieces_found == 3:
                print(f"The character reached the legendary "
                      f"artifact with {energy:.2f} energy left.")
                break
    elif command == "desert":
        energy -= 15
    elif command == "forest":
        energy += 7

    if energy <= 0:
        print(f"The character is too exhausted to carry on with the journey.")
        break

    command = input()

else:
    print(f"The character could not find all the pieces and needs "
          f"{3 - pieces_found} more to complete the legendary artifact.")