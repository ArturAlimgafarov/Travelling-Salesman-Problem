# Travelling Salesman Problem (TSP)
___
## Description
The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: 
"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits 
each city exactly once and returns to the origin city?"

## Computational complexity
The problem has been shown to be NP-hard (more precisely, it is complete for the complexity class FPNP; see function 
problem), and the decision problem version ("given the costs and a number x, decide whether there is a round-trip route 
cheaper than x") is NP-complete. The bottleneck travelling salesman problem is also NP-hard. The problem remains NP-hard
even for the case when the cities are in the plane with Euclidean distances, as well as in a number of other restrictive
cases. Removing the condition of visiting each city "only once" does not remove the NP-hardness, since in the planar 
case there is an optimal tour that visits each city only once (otherwise, by the triangle inequality, a shortcut that 
skips a repeated visit would not increase the tour length).

## Methods
### Ant colony oprimization algorithm
In computer science and operations research, the ant colony optimization algorithm (ACO) is a probabilistic technique 
for solving computational problems which can be reduced to finding good paths through graphs. Artificial ants stand for 
multi-agent methods inspired by the behavior of real ants. The pheromone-based communication of biological ants is often
the predominant paradigm used. Combinations of artificial ants and local search algorithms have become a method of 
choice for numerous optimization tasks involving some sort of graph, e.g., vehicle routing and internet routing.

![Ant Colony Algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Aco_branches.svg/400px-Aco_branches.svg.png)

### Simulated annealing
Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. 
Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem. It is often used when the search space is discrete (for example the traveling salesman problem, the boolean satisfiability problem, protein structure prediction, and job-shop scheduling). For problems where finding an approximate global optimum is more important than finding a precise local optimum in a fixed amount of time, simulated annealing may be preferable to exact algorithms such as gradient descent or branch and bound.
The name of the algorithm comes from annealing in metallurgy, a technique involving heating and controlled cooling of a material to alter its physical properties. Both are attributes of the material that depend on their thermodynamic free energy. Heating and cooling the material affects both the temperature and the thermodynamic free energy or Gibbs energy. Simulated annealing can be used for very hard computational optimization problems where exact algorithms fail; even though it usually achieves an approximate solution to the global minimum, it could be enough for many practical problems.
The problems solved by SA are currently formulated by an objective function of many variables, subject to several constraints. In practice, the constraint can be penalized as part of the objective function.
Similar techniques have been independently introduced on several occasions, including Pincus (1970), Khachaturyan et al (1979, 1981), Kirkpatrick, Gelatt and Vecchi (1983), and Cerny (1985). In 1983, this approach was used by Kirkpatrick, Gelatt Jr., Vecchi,[5] for a solution of the traveling salesman problem. They also proposed its current name, simulated annealing.
This notion of slow cooling implemented in the simulated annealing algorithm is interpreted as a slow decrease in the probability of accepting worse solutions as the solution space is explored. Accepting worse solutions allows for a more extensive search for the global optimal solution. In general, simulated annealing algorithms work as follows. The temperature progressively decreases from an initial positive value to zero. At each time step, the algorithm randomly selects a solution close to the current one, measures its quality, and moves to it according to the temperature-dependent probabilities of selecting better or worse solutions, which during the search respectively remain at 1 (or positive) and decrease towards zero.
The simulation can be performed either by a solution of kinetic equations for density functions or by using the stochastic sampling method. The method is an adaptation of the Metropolis–Hastings algorithm, a Monte Carlo method to generate sample states of a thermodynamic system, published by N. Metropolis et al. in 1953.

![Simulated Annealing Visualization](https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif)