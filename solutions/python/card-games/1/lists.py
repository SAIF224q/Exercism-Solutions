"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    rounds = [number, number + 1, number + 2]
    return rounds



def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2



def list_contains_round(rounds, number):
    return number in rounds



def card_average(hand):
    average = sum(hand)/len(hand)
    return average



def approx_average_is_average(hand):
    average_1 = card_average(hand)
    average_2 = (hand[0] + hand[-1]) / 2
    average_3 = hand[int(len(hand)/2)]
    if average_1 == average_2 or average_1 == average_3:
        return True
    else:
        return False



def average_even_is_average_odd(hand):
    even = hand[1::2]
    odd = hand[0::2]
    odd_average = sum(even)/len(even)
    even_average = sum(odd)/len(odd)
    return odd_average == even_average



def maybe_double_last(hand):
    new_hand = []
    if hand[-1] == 11:
        for i in hand:
            if i == 11:
                new_hand += [i*2]
            else:
                new_hand += [i]
        return new_hand
    else:
        return hand
