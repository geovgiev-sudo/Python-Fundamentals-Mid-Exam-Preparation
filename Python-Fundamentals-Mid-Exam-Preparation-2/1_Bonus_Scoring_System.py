from sys import maxsize
from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
bonus = int(input())
max_bonus = 0
lectures_attended = 0

for student in range(1, number_of_students + 1):
    attendance = int(input())
    total_bonus = attendance / number_of_lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures_attended = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lectures_attended} lectures.")