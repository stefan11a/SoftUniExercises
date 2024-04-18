period = int(input())

untreated = 0
treated = 0
doctors = 7

for day_of_period in range(1, period + 1):
    patients = int(input())
    if day_of_period % 3 == 0 and untreated > treated:
        doctors += 1
    if patients <= doctors:
        treated += patients
    else:
        untreated += patients - doctors
        treated += doctors

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
