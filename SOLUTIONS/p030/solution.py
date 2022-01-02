from typing import List

def get_capacity_of_valleys(profile: List[int]) -> int:
    """Return the capacity of al valley in the profile.

    >>> get_capacity_of_valleys([2, 1, 2])
    1
    >>> get_capacity_of_valleys([2, 0, 1, 0, 1, 0, 3])
    8
    >>> get_capacity_of_valleys([3, 2, 1, 0])
    0
    >>> get_capacity_of_valleys([0, 1, 1, 5])
    0
    >>> get_capacity_of_valleys([0, 1, 2, 2, 2, 1, 0])
    0
    >>> get_capacity_of_valleys([2, 1, 3, 0, 2])
    3
    >>> get_capacity_of_valleys([3, 0, 1, 3, 0, 5])
    8
    """
    capacity = 0
    #foreward
    maximum = -1
    in_valley = False
    for i in range(1, len(profile)):
        if in_valley: #searching for the opposite boundery
            if profile[i] >= profile[maximum]:
                capacity += sum(profile[maximum] - height for height in profile[maximum+1:i])
                in_valley = False
        else:#  searching for maximum
            if profile[i-1] > profile[i]:
                maximum = i-1
                in_valley = True
    # backwards if in_valley is true 
    if in_valley:
        in_valley = False
        stop = maximum
        for i in range(len(profile)-2, stop-1, -1):
            if in_valley: #searching for the opposite boundery
                if profile[i] >= profile[maximum]:
                    capacity += sum(profile[maximum] - height for height in profile[i+1:maximum])
                    in_valley = False
            else:#  searching for maximum
                if profile[i+1] > profile[i]:
                    maximum = i+1
                    in_valley = True
    return capacity
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
