import numpy as np
from simulated_annealing import simAnnealing

nodes = np.loadtxt('data_10.txt')
nodes = [n[1:] for n in nodes]
print(nodes)

print(simAnnealing(nodes))