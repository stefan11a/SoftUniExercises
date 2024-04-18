numbers = input().split(", ")

print(f"Positive: {', '.join([number for number in numbers if int(number) >=0])}")
print(f"Negative: {', '.join([number for number in numbers if int(number) <0])}")
print(f"Even: {', '.join([number for number in numbers if int(number) % 2 == 0])}")
print(f"Odd: {', '.join([number for number in numbers if int(number) % 2 != 0])}")