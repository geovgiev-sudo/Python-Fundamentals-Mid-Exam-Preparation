elements = input().split()
number_of_moves = 0

while True:
    command = input()
    if command == "end":
        break
    number_of_moves += 1

    i1, i2 = map(int, command.split())

    if i1 == i2 or i1 < 0 or i2 < 0 or i1 >= len(elements) or i2 >= (len(elements)):
        middle_index = int(len(elements) // 2)
        punishment = f"-{number_of_moves}a"
        elements.insert(middle_index, punishment)
        elements.insert(middle_index, punishment)
        print(f"Invalid input! Adding additional elements to the board")
        continue

    if elements[i1] == elements[i2]:
        element_to_remove = elements[i1]
        if i1 > i2:
            elements.pop(i1)
            elements.pop(i2)
        elif i2 > i1:
            elements.pop(i2)
            elements.pop(i1)

        print(f"Congrats! You have found matching elements - {elements[i1]}!")

    elif elements[i1] != elements[i2]:
        print(f"Try again!")

    if not elements:
        print(f"You have won in {number_of_moves} turns!")
        break

if elements:
    print("Sorry you lose :(")
    print(" ".join(elements))
