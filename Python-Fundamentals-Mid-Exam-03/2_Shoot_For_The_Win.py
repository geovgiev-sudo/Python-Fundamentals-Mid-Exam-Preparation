# # КАКВО ПРАВИМ, АКО ИМАМЕ ДВА ЕДНАКВИ ИДНЕКСА?
#
#
# integers = list(map(int, input().split()))
# command = input()
# shot_indexes = []
# shots = 0
# while command != "End":
#     command = command.split()
#     i = int(command[0])
#     if 0 <= i < len(integers):
#         old_value = integers[i]
#         if i not in shot_indexes:
#             shots += 1
#             shot_indexes.append(i)
#             integers[i] = -1
#             for num in range(len(integers)):
#                 if integers[num] > old_value and integers[num] != - 1:
#                     integers[num] -= old_value
#                 elif integers[num] <= old_value and integers[num] != - 1:
#                     integers[num] += old_value
#
#
#     command = input()
#
# integers_str = list(map(str, integers))
# print(f"Shot targets: {shots} -> {' '.join(integers_str)}")



integers = list(map(int, input().split()))
command = input()

shots = 0
while command != "End":
    command = command.split()
    i = int(command[0])
    if 0 <= i < len(integers):
        shots += 1
        old_value = integers[i]
        integers[i] = -1
        for num in range(len(integers)):
            if integers[num] > old_value and integers[num] != - 1:
                integers[num] -= old_value
            elif integers[num] <= old_value and integers[num] != - 1:
                integers[num] += old_value


    command = input()

integers_str = list(map(str, integers))
print(f"Shot targets: {shots} -> {' '.join(integers_str)}")