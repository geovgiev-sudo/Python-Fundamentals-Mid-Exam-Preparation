integers = list(map(int, input().split()))
integers_sum = sum(integers)
average_value = integers_sum / len(integers)
top_5 = []

for integer in integers:
    if integer > average_value:
        top_5.append(integer)

if len(top_5) == 0:
    print(f"No")
else:
    top_5.sort(reverse=True)
    top_5_str = list(map(str, top_5))
    print(f"{' '.join(top_5_str[:5])}")