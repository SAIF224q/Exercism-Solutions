"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]



def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):

    treasure_coord = azara_record[1]


    location_coord = rui_record[1]


    normalized_treasure = (treasure_coord[0], treasure_coord[1:]) if len(treasure_coord) > 1 else (treasure_coord,)


    normalized_location = ''.join(location_coord)

    return normalized_treasure[0] + normalized_treasure[1] == normalized_location



def create_record(azara_record, rui_record):

    azara_coord = azara_record[1]


    rui_coord = rui_record[1]

    normalized_azara = (azara_coord[0], azara_coord[1:]) if len(azara_coord) > 1 else (azara_coord,)


    normalized_rui = ''.join(rui_coord)


    if normalized_azara[0] + normalized_azara[1] == normalized_rui:

        return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
    else:
        return "not a match"



def clean_up(combined_record_group):
    report = ""
    
    for record in combined_record_group:
        cleaned_record = (record[0], record[2], record[3], record[4])
        report += f"{cleaned_record}\n"
    
    return report

