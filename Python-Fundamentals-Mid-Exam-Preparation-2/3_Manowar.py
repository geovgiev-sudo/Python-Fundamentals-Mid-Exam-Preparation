pirate_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
hp_max_capacity = int(input())

while True:
    command = input()
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_status)}")
        print(f"Warship status: {sum(warship_status)}")
        break
    command = command.split()
    action = command[0]
    if action == "Fire":
        i = int(command[1])
        damage = int(command[2])
        if 0 <= i < len(warship_status):
            warship_status[i] -= damage
            if warship_status [i] <= 0:
                print(f"You won! The enemy ship has sunken.")
                break
    elif action == "Defend":
        i_start = int(command[1])
        i_end = int(command[2])
        damage = int(command[3])
        ship_is_sunken = False
        if 0 <= i_start < len(pirate_status) and 0 <= i_end < len(pirate_status):
            for i in range(i_start, i_end + 1):
                pirate_status[i] -= damage
                if pirate_status[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    ship_is_sunken = True
                    break
            if ship_is_sunken:
                break

    elif action == "Repair":
        i = int(command[1])
        healed_hp = int(command[2])
        if 0 <= i < len(pirate_status):
            current_hp = pirate_status[i] # просто за удобство и четимост
            old_health = current_hp
            current_hp += healed_hp
            if current_hp > hp_max_capacity:
                current_hp = hp_max_capacity
            pirate_status[i] = current_hp
    elif action == "Status":
        repair_needed = 0
        for section in pirate_status:
            if section < hp_max_capacity * 0.20:
                repair_needed += 1
        print(f"{repair_needed} sections need repair.")

