phone_book = {}

while True:

    contact = input().split('-')

    if len(contact) == 1:
        curr_contact = int(contact[0])
        for n in range(curr_contact):
            check_contact = input()
            if check_contact in phone_book.keys():
                print(f"{check_contact} -> {phone_book[check_contact]}")
            else:
                print(f'Contact {check_contact} does not exist.')
        break
    else:
        for i in range(0, len(contact), 2):
            name = contact[i]
            phone = contact[i + 1]
            phone_book[name] = phone

# while True:
#     entry = input()
#
#     if '-' not in entry:
#         break
#     name, phone_number = entry.split('-')
#     phone_book[name] = phone_number
#
# searches = int(entry)
#
# for search in range(searches):
#     contact = input()
#     if contact in phone_book:
#         print(f"{contact} -> {phone_book[contact]}")
#     else:
#         print(f'Contact {contact} does not exist.')
#