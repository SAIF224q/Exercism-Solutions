"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for i in items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory



def add_items(inventory, items):
    inventory_items = inventory
    for i in items:
        if i in inventory_items:
            inventory_items[i] += 1
        else:
            inventory_items[i] = 1
    return inventory_items



def decrement_items(inventory, items):
    for i in items:
        if i in inventory:
            if inventory[i] == 0:
                pass
            else:
                inventory[i] -= 1
    return inventory



def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory



def list_inventory(inventory):
    list_of_inventory = []
    for key, value in inventory.items():
        if value > 0:
            list_of_inventory.append((key,value))   
    return list_of_inventory
        

