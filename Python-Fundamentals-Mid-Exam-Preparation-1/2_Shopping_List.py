groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            item_index = groceries.index(old_item)
            # groceries.remove(old_item)
            # old_item = new_item
            # groceries.insert(item_index, new_item)
            groceries[item_index] = new_item

    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command = input()

print(", ".join(groceries))