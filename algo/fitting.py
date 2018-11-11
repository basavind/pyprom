def mark_fitting(places):
    result = []
    for place in places:
        if is_place_underfitted(place):
            result.append(place + ({
                'type': 'underfitted',
                'color': 'blue',
            },))
        if is_place_fitted(place):
            result.append(place + ({
                'type': 'fitted',
                'color': 'green',
            },))
        if is_place_overfitted(place):
            result.append(place + ({
                'type': 'overfitted',
                'color': 'red',
            },))
    return result


def is_place_underfitted(place):
    in_place, out_place = place
    if len(in_place) < len(out_place):
        return True
    return False


def is_place_fitted(place):
    in_place, out_place = place
    if len(in_place) == len(out_place):
        return True
    return False


def is_place_overfitted(place):
    in_place, out_place = place
    if len(in_place) > len(out_place):
        return True
    return False
