day_from_week = input()
ticket_price = 0

if day_from_week == 'Monday':
    ticket_price = 12
elif day_from_week == 'Tuesday':
    ticket_price = 12
elif day_from_week == 'Wednesday':
    ticket_price = 14
elif day_from_week == 'Thursday':
    ticket_price = 14
elif day_from_week == 'Friday':
    ticket_price = 12
elif day_from_week == 'Saturday':
    ticket_price = 16
elif day_from_week == 'Sunday':
    ticket_price = 16

print(ticket_price)
