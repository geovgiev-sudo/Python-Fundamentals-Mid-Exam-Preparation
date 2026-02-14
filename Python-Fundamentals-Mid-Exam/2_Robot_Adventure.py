integers = list(map(int, input().split("|")))
total_items_collected = 0

while True:
    command = input()
    if command == "Adventure over":
        break

    if "Step" in command:
        command = command.split("$")
        action = command[0]
        start_index = int(command[1])
        step = int(command[2])
        index_to_remove = 0

        if 0 <= start_index < len(integers):
            if action == "Step Backward":
                index_to_remove = (start_index - step) % len(integers)
            elif action == "Step Forward":
                index_to_remove = (start_index + step) % len(integers)
            total_items_collected += integers[index_to_remove]
            integers[index_to_remove] = 0

    else:
        command = command.split()
        action = command[0]
        if action == "Double":
            index = int(command[1])
            if 0 <= index < len(integers):
                integers[index] *= 2

        elif action == "Switch":
            integers.reverse()


print(f"{' - '.join(map(str, integers))}")
print(f"Robo finished the adventure with {total_items_collected} items!")