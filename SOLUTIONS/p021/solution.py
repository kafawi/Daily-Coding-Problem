"""Test
>>> find_minimum_number_of_rooms([(30, 75), (0, 50), (60, 150)])
2

>>> find_minimum_number_of_rooms([(0,1),(0,4),(1,2),(7,9),(3,6),(5,8)])
2

>>> find_minimum_number_of_rooms([])
0

>>> find_minimum_number_of_rooms([(0,4),(3,7),(2,6),(1,5)])
4

>>> find_minimum_number_of_rooms([(0,1),(2,3),(1,2),(3,4),(5,10)])
1

>>> find_minimum_number_of_rooms([(-20, 20),(-10,10),(-5,5),(0,0)])
3
"""

def find_minimum_number_of_rooms(lecture_periods: [(int, int)]) -> int:
    time2delta_lectures : dict = {}
    for start, end in lecture_periods:
        if start not in time2delta_lectures : time2delta_lectures[start] = 0
        if end not in time2delta_lectures: time2delta_lectures[end] = 0
        time2delta_lectures[start] += 1
        time2delta_lectures[end] -= 1

    nlectures = 0
    min_rooms = 0
    for time, delta_lecture in sorted(time2delta_lectures.items(), key=lambda x:x[0]): 
        nlectures += delta_lecture
        # the minimum of needed rooms is determin by the maximum number of parrallel lectures
        min_rooms = max(min_rooms, nlectures)
    return min_rooms


if __name__ == "__main__":
    import doctest
    doctest.testmod()
