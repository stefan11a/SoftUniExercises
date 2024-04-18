months = int(input())

electricity_bill = 0
water_bill = 20
internet_bill = 15
total_others = 0
total_electricity = 0

for _ in range(1, months + 1):
    electricity_bill = float(input())
    total_electricity += electricity_bill
    total_others += (electricity_bill + water_bill + internet_bill) * 1.2
    total_spends = electricity_bill + water_bill + internet_bill + total_others / months

    total_water = months * water_bill
    total_internet = months * internet_bill

    average_spends = (total_water + total_internet + total_electricity + total_others) / months


print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {total_others:.2f} lv')
print(f'Average: {average_spends:.2f} lv')
