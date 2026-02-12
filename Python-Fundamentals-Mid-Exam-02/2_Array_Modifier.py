array = list(map(int, input().split()))

command = input()

while command != "end":
    command = command.split()
    action = command[0]

    if action == "decrease":
        for i in range(len(array)):
            array[i] -= 1
        command = input()
        continue

    i1 = int(command[1])
    i2 = int(command[2])

    if action == "swap":
        array[i1], array[i2] = array[i2], array[i1]

    elif action == "multiply":
        result = array[i1] * array[i2]
        array[i1] = result

    command = input()

array_str = list(map(str, array))
print(f"{', '.join(array_str)}")