import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        balls = []
        for i in kwargs:
            k = 1
            while k <= kwargs[i]:
                balls.append(i)
                k += 1
        print(balls)
        print(kwargs)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    return None