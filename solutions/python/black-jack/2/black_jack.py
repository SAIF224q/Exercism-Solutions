"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""



def value_of_card(card):

    face = {"J","Q","K"}

    if card in face:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    value_of_one = value_of_card(card_one)
    value_of_two = value_of_card(card_two)
    if value_of_one > value_of_two:
        return card_one
    elif value_of_one < value_of_two:
        return card_two
    else:
        return (card_one , card_two)


def value_of_ace(card_one, card_two):
    value_of_one = value_of_card(card_one)
    value_of_two = value_of_card(card_two)

    sum_of_values = value_of_one + value_of_two
    
    if card_one == "A" or card_two == "A":
        return 1
    elif sum_of_values + 11 > 21:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    ten_cards = {"10","J","K","Q"}
    ace_presence = card_one == "A" or card_two == "A"
    ten_card_presence = card_one in ten_cards or card_two in ten_cards

    return ace_presence and ten_card_presence


def can_split_pairs(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    return card_one_value == card_two_value


def can_double_down(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    sum_value = card_one_value + card_two_value

    return sum_value in {9,10,11}
