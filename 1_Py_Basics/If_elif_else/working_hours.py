hour = int(input())
day_from_week = input()

if day_from_week == 'Monday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day_from_week == 'Tuesday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day_from_week == 'Wednesday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day_from_week == 'Thursday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day_from_week == 'Friday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day_from_week == 'Saturday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')