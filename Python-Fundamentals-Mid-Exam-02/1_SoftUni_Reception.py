employee_efficiency1 = int(input())
employee_efficiency2 = int(input())
employee_efficiency3 = int(input())
number_of_students = int(input())
hours = 0
total_efficiency = employee_efficiency1 + employee_efficiency2 + employee_efficiency3

while number_of_students:
    hours += 1
    if hours % 4 == 0 and hours != 0:
        continue
    number_of_students -= total_efficiency
    if number_of_students <= 0:
        break

time = hours
print(f"Time needed: {time}h.")