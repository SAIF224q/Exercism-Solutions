def square_of_sum(number):
    sum_of_num = sum(range(1,number+1))
    return sum_of_num ** 2


def sum_of_squares(number):
    sum_of_sqNum = number * (number + 1) * (2 * number + 1) // 6
    return sum_of_sqNum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

