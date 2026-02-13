rooms = input().split("|")
health = 100
bitcoins = 0
room_counter = 0

for room in rooms:
    action = room.split()
    command = action[0]
    number = int(action[1])
    room_counter += 1

    if command == "potion":
        old_health = health
        health += number
        if health > 100:
            health = 100
        healed = health - old_health
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break
else:
    print(f"You've made it!\n"
        f"Bitcoins: {bitcoins}\n"
        f"Health: {health}")