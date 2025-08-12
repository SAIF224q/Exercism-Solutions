"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time):
    """This Function takes actual minute the lasagna has been in
    the oven and returns how many minutes the lasanga still needs to bake"""
    Time_remain = EXPECTED_BAKE_TIME - time
    return Time_remain


def preparation_time_in_minutes(number_of_layers):
    """Takes numbers of layers you want to add to the lasagna as a argument
    and return how mant minutes you would spend making them"""
    preparation_time_in_minutes = number_of_layers * 2
    return preparation_time_in_minutes

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    Total_baking_time = number_of_layers*2 + elapsed_bake_time
    return Total_baking_time
