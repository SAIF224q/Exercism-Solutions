"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """



def read_notes(notes):
    cart = dict()
    for i in notes:
        cart[i] = 1
    return cart
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """


def update_recipes(ideas, recipe_updates):
    ideas.update(dict(recipe_updates))
    return ideas
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """



def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """



def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}

    # Populate the fulfillment cart with quantity, aisle, and refrigeration
    for item, quantity in cart.items():
        aisle, refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]

    sort_fulfillment_cart = dict(sorted(fulfillment_cart.items(), reverse=True))

    return sort_fulfillment_cart
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """


def update_store_inventory(fulfillment_cart, store_inventory):
    for key, value in fulfillment_cart.items():
        store_inventory[key][0] = store_inventory[key][0] - value[0] 
        if store_inventory[key][0] <= 0:
            store_inventory[key][0] = "Out of Stock"

    return store_inventory
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
