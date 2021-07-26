from random import random

def monte_carlo_pi(precition :float):
    pi :float = 10
    total_count :int = 0
    circle_count :int = 0
    count_precition :int = 0
    while count_precition < int(1/precition):
        old_pi :float = pi
        for _ in range(int(4/precition)):
            x :float = random()
            y :float = random()
            if x*x + y*y < 1:
                circle_count += 1
        total_count += int(4/precition)
        pi = 4*circle_count/total_count
        if abs(round(old_pi/precition) - round(pi/precition)) == 0:
            count_precition +=1
        else:
            count_precition = 0
    return pi


if __name__ == "__main__":
    from math import pi
    print(pi)
    print(monte_carlo_pi(10**-3))