days_holiday = int(input())
room = input()
review = input()

final_price = 0
nights = days_holiday - 1

if days_holiday < 10:
    if room == 'room for one person':
        final_price = nights * 18
    if room == 'apartment':
        final_price = (nights * 25) * 0.7
    if room == 'president apartment':
        final_price = (nights * 35) * 0.9

elif 10 < days_holiday < 15:
    if room == 'room for one person':
        final_price = nights * 18
    if room == 'apartment':
        final_price = (nights * 25) * 0.65
    if room == 'president apartment':
        final_price = (nights * 35) * 0.85

else:
    if room == 'room for one person':
        final_price = nights * 18
    if room == 'apartment':
        final_price = (nights * 25) * 0.5
    if room == 'president apartment':
        final_price = (nights * 35) * 0.8

if review == 'positive':
    final_price = final_price * 1.25
elif review == 'negative':
    final_price = final_price * 0.9

print(f'{final_price:.2f}')
