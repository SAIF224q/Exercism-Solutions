def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    proper_diviser_sum = sum(diviser for diviser in range(1,number) if number % diviser == 0 )

    if number == proper_diviser_sum:
        return "perfect"
    elif number < proper_diviser_sum :
        return "abundant"
    else:
        return "deficient"
    
    
