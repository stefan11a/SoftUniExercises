bottles = int(input())

total_plates = 0
total_pots = 0
washes_count = 0
total_detergent = bottles * 750

while total_detergent >= 0:
    dishes = input()
    washes_count += 1
    if dishes != 'End':
        dishes = int(dishes)

        if washes_count % 3 == 0:
            total_detergent -= dishes * 15
            total_pots += dishes
        else:
            total_detergent -= dishes * 5
            total_plates += dishes
    else:
        print(f"Detergent was enough!")
        print(f"{total_plates} dishes and {total_pots} pots were washed.")
        print(f"Leftover detergent {total_detergent} ml.")
        break
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
