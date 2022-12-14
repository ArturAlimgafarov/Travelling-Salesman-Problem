from math import dist, exp
from random import randint, shuffle, random


def simAnnealing(nodes):
    def getLength(p):
        return sum([dist(nodes[p[i]], nodes[p[i + 1]]) for i in range(len(p) - 1)])

    def modify(p):
        i, j = randint(0, len(p) - 1), randint(0, len(p) - 1)
        p[i], p[j] = p[j], p[i]
        p.append(p[0])

    # params
    iterCount: int = 20
    coolingRate: float = 0.999
    eps: float = 1e-5
    temperature: float = 100.0

    # init salesperson route
    path = list(range(len(nodes)))
    shuffle(path)
    path.append(path[0])

    while temperature >= eps:
        for _ in range(iterCount):
            mdf = path[:-1]
            modify(mdf)
            diff = getLength(mdf) - getLength(path)
            if (diff <= 0) or (diff > 0 and exp(-diff / temperature) >= random()):
                path = mdf
        temperature *= coolingRate

    return path, getLength(path)
