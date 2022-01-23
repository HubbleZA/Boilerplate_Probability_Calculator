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
        self.data = hat

    def draw(self, draws):
        editlist = copy.deepcopy(self.data)
        chosenlist = []
        i = 0
        while i < draws:
            pull = random.randint(0, (len(editlist) - 1))
            chosenlist.append(editlist.pop(pull))
            self.data.pop(pull)
            i += 1
        return chosenlist

    def contents(self):
        editlist = copy.deepcopy(self.data)
        print(editlist)
        return editlist

    def __repr__(self):
        return str(self.data)

    def probability(self, balls, draws, experiments):
        editlist = []
        chosenlist = []
        exp = 0
        times = 0
        if draws > len(self.data):
            prob = 1
        else:
            while exp < experiments:
                editlist = copy.deepcopy(self.data)
                i = 0
                while i < draws:
                    pull = random.randint(0, (len(editlist)-1))
                    chosenlist.append(editlist.pop(pull))
                    i += 1
                chosenlist.sort()
                picked = Counter(chosenlist)
                picked = dict(picked)
                chosenlist = []
                shared_items = {k: balls[k] for k in balls if k in picked and balls[k] == picked[k]}
                if shared_items == balls:
                    times += 1
                exp += 1
            prob = times / exp
        return prob

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = Hat.probability(hat, expected_balls, num_balls_drawn, num_experiments)
    #print(prob)
    return prob