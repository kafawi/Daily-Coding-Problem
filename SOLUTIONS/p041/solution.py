"""Test

    >>> calculate_itinerary([], 'A') == None
    True

    >>> calculate_itinerary([('A', 'B')], 'A')
    ['A', 'B']

    >>> calculate_itinerary([('B', 'A')], 'A') == None
    True

    >>> calculate_itinerary([('A', 'B')], 'C') == None
    True

    >>> calculate_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    >>> calculate_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None
    True

    >>> calculate_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
    ['A', 'B', 'C', 'A', 'C']

"""
# my type of airport
from collections import defaultdict
Airport = str


def _calculate_itinerary(flights: list[tuple[Airport, Airport]], start: Airport) -> list[Airport] | None:
    if not flights:
        return [start]
    for i, flight in enumerate(flights):
        origin, destination = flight
        if origin == start:
            route = _calculate_itinerary(
                flights[:i] + flights[i+1:], destination)
            if route:
                return [start] + route
    return None


def calculate_itinerary(flights: list[tuple[Airport, Airport]], start: Airport) -> list[Airport] | None:
    if not flights:
        return None
    return _calculate_itinerary(sorted(flights), start)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
