days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
third_daily_plunder = 0
total_plundered = 0

for day in range(1, days + 1):
    total_plundered += daily_plunder

    if day % 3 == 0:
        third_daily_plunder = daily_plunder * 0.50
        total_plundered += third_daily_plunder

    if day % 5 == 0:
        total_plundered -= total_plundered * 0.30

if total_plundered >= expected_plunder:
    print(f"Ahoy! {total_plundered:.2f} plunder gained.")
elif total_plundered < expected_plunder:
    percentage = total_plundered / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

