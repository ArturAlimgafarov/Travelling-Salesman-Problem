import numpy as np
from simulated_annealing import simAnnealing
from ant_colony import antColony

# load data from file
nodes = np.loadtxt('data_10.txt')
nodes = [n[1:] for n in nodes]

# testing algorithms
print(simAnnealing(nodes))
print(antColony(nodes))
