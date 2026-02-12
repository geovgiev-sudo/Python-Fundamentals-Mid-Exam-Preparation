people = int(input())
lift_state = list(map(int, input().split()))
max_wagon_capacity = 4
total_train_capacity = max_wagon_capacity * len(lift_state)
index = 0
while people > 0 and index < len(lift_state):
    available_seats = max_wagon_capacity - lift_state[index]
    current_wagon_load = lift_state[index]
    people_boarding = available_seats - lift_state[index]
    lift_state[index] += people_boarding
    people -= people_boarding
    index += 1

lift_state_str = list(map(str, lift_state))

if people == 0 and sum(lift_state) < total_train_capacity:
    print(f"The lift has empty spots!\n"
          f"{' '.join(lift_state_str)}")

elif people > 0 and sum(lift_state) == total_train_capacity:
    print(f"There isn't enough space! {people} people in a queue!\n"
          f"{' '.join(lift_state_str)}")

elif people == 0 and sum(lift_state) == total_train_capacity:
    print(f"{' '.join(lift_state_str)}")





#for i in range(len(lift_state)):
#     available_seats = max_wagon_capacity - lift_state[i]
#     current_wagon_load = lift_state[i]
#     people_boarding = available_seats - lift_state[i]
#     lift_state[i] += people_boarding
#     people -= people_boarding









# 1. make an integer list from string
# 2. make an integer list from string
# lift_state = [int(integer) for integer in input().split()]
# lift_state = list(map(int, input().split()))