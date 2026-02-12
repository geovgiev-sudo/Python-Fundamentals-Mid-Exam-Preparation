targets = list(map(int, input().split()))
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    i = int(command[1])

    if action == "Shoot":
        if 0 <= i < len(targets):
            power = int(command[2])
            targets[i] = targets[i] - power
            if targets[i] <= 0:
                targets.pop(i)

    elif action == "Add":
        if 0 <= i < len(targets):
            value = int(command[2])
            targets.insert(i, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(command[2])
        if i - radius >= 0 and i + radius < len(targets):
            start_remove = i - radius
            end_remove = i + radius + 1
            del targets[start_remove:end_remove]
            # for num in to_remove:
            #     if num in targets:
            #         targets.remove(num)

            # targets = [num for num in targets if num not in to_remove] # Пробвай с list comprehension



        # elif action == "Strike":
        #     radius = int(command[2])
        #     # Check if the whole range is within the fence [cite: 16]
        #     if i - radius >= 0 and i + radius < len(targets):
        #         # The total number of targets to remove is (radius * 2) + 1 [cite: 15]
        #         # (The center target + targets before + targets after)
        #         number_of_targets_to_remove = (radius * 2) + 1
        #
        #         # The starting index for removal [cite: 15]
        #         start_index = i - radius
        #
        #         # Pop the same index repeatedly
        #         for _ in range(number_of_targets_to_remove):
        #             targets.pop(start_index)
        #     else:
        #         print("Strike missed!")



        else:
            print("Strike missed!")



    command = input()
targets_str = list(map(str, targets))
print("|".join(targets_str))