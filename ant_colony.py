from math import dist
import random


def antColony(nodes):
    # params
    pheromone: float = 0.2
    alpha: float = 1.0
    beta: float = 2.0
    evaporation: float = 0.25
    q: float = 1.0
    antCount: int = 10
    iterCount: int = 10

    def getLength(p):
        return sum([dist(nodes[p[i]], nodes[p[i + 1]]) for i in range(len(p) - 1)])

    def calcProbs(vertex, vertices):
        p = []
        for v in vertices:
            a, b = min(v, vertex), max(v, vertex)
            d, ph = edges[(a, b)]['distance'], edges[(a, b)]['pheromone']
            p.append((ph ** alpha) * ((1 / d) ** beta))
        p = [item / sum(p) for item in p]
        return p

    def findPath(start, vertices):
        path = []
        t = start
        for _ in range(len(vertices)):
            path.append(t)
            vertices.remove(t)
            probs = calcProbs(t, vertices)
            p = [(sum(probs[:i]), sum(probs[:i]) + probs[i]) for i in range(len(probs))]
            u = random.random()
            for i in range(len(p)):
                if (p[i][0] < u < p[i][1]):
                    t = vertices[i]
        path.append(start)
        return path

    def updatePheromones(paths):
        for i in edges:
            edges[i]['pheromone'] *= evaporation
        for (path, _) in paths:
            for i in range(len(path) - 1):
                a, b = min(path[i], path[i + 1]), max(path[i], path[i + 1])
                edges[(a, b)]['pheromone'] += q / edges[(a, b)]['distance']

    edges = dict()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edges[(i, j)] = {
                'distance': dist(nodes[i], nodes[j]),
                'pheromone': pheromone
            }

    # algorithm
    best = []
    for _ in range(iterCount):
        paths = []
        taboo = list(range(len(nodes)))  # [0, 1, ..., dataCount - 1]
        for _ in range(antCount):
            k = random.choice(taboo)
            taboo.remove(k)
            path = findPath(k, list(range(len(nodes))))
            paths.append((path, getLength(path)))
        best.append(min(paths, key=lambda x: x[1]))
        updatePheromones(paths)
    solution = min(best, key=lambda x: x[1])
    return solution