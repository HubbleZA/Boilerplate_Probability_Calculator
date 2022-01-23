import copy
import random
from collections import Counter


# Consider using the modules imported above.
class Hat:
    def __init__(self, **kwargs):
        hat = []
        for i in kwargs:
            k = 1
            while k <= kwargs[i]:
                hat.append(i)
                k += 1
        self.contents = hat

    def draw(self, draws):
        chosenlist = []
        i = 0
        if draws > len(self.contents):
            return self.contents
        while i < draws:
            pull = random.randint(0, (len(self.contents) - 1))
            chosenlist.append(self.contents.pop(pull))
            i += 1
        return chosenlist

    def __repr__(self):
        return str(self.contents)

    def probability(self, balls, draws, experiments):
        times = 0
        exp = 0
        prob = 0
        uneditlist = copy.deepcopy(self.contents)
        while exp < experiments:
            chosenlist = self.draw(draws)
            self.contents = copy.deepcopy(uneditlist)
            chosenlist.sort()
            picked = Counter(chosenlist)
            picked = dict(picked)
            shared_items = {k: balls[k] for k in balls if k in picked and balls[k] <= picked[k]}
            if shared_items == balls:
                times += 1
            exp += 1
        prob = times / exp
        return prob


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = Hat.probability(hat, expected_balls, num_balls_drawn, num_experiments)
    return prob
