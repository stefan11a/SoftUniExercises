def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]

    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_repetition = match_symbol * uninterrupted_match_length
            if winning_repetition in left_part and winning_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]

for curr_ticket in tickets:
    print(check_ticket(curr_ticket))
