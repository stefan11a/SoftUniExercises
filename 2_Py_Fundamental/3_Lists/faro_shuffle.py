deck_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_cards) // 2
    left_part = deck_cards[0:middle_of_deck]
    right_part = deck_cards[middle_of_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_cards = deck_after_shuffling
print(deck_after_shuffling)