def loading_bar(number):
    loading_list = []
    integer = number // 10
    for i in range(0, integer):
        loading_list.append('%')
    for j in range(0, (10 - integer)):
        loading_list.append('.')
    loading_list = ''.join(loading_list)
    if number != 100:
        print(f'{number}% [{loading_list}]')
        print('Still loading...')
    else:
        print('100% Complete!')
        print('[%%%%%%%%%%]')


the_number = int(input())
loading_bar(the_number)