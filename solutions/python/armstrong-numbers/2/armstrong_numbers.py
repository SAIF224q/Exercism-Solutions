def is_armstrong_number(number):
    number_list = list(str(number))
    power = len(number_list)
    return sum([int(i)**power for i in number_list]) == number
