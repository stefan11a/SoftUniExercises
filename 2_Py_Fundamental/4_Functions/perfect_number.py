def perfect_num(number):

    divisors_list = []
    for i in range(1, number):
        if number % i == 0:
            divisors_list.append(i)
    if sum(divisors_list) == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


the_number = int(input())
perfect_num(the_number)
