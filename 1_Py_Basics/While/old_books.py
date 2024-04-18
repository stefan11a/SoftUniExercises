book_name = input()
books = 0
is_book_found = False
current_book = input()

while current_book != 'No More Books':

    if current_book == book_name:
        is_book_found = True
        print(f'You checked {books} books and found it.')
        break
    else:
        books += 1
        current_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {books} books.')
