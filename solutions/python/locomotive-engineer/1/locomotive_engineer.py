"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagonIDs):
    wagonIDs_list = []
    for i in wagonIDs:
        wagonIDs_list.append(i)
    return wagonIDs_list
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """



def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first,second,third, *rest = each_wagons_id
    combined_IDs = third,*missing_wagons, *rest,first,second
    return list(combined_IDs)
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """



def add_missing_stops(dic, **missing_stops):
    missing_stops_list = []
    for stop in missing_stops.values():
        missing_stops_list.append(stop)
    missing_stops_dic = {"stops":missing_stops_list}
    dic.update(missing_stops_dic)
    return dic
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """



def extend_route_information(route, more_route_information):
    final_route = {**route, **more_route_information}
    return final_route
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """



def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
