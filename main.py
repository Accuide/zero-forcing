import random

from src.graph import Graph
from src.algorithms.brute_force import brute_force
from src.algorithms.least_degree import least_degree
from src.algorithms.greatest_degree import greatest_degree

def generate_random_graph(size: int, edge_probability: float):
    g = Graph(size, [[False for _ in range(size)] for _ in range(size)])

    for j in range(size):
        for i in range(j):
            if random.random() < edge_probability:
                g.add_edge(i, j)
    
    for j in range(size):
        if g.get_degree(j) == 0:
            i = random.randint(0, size - 2)
            if i >= j:
                i += 1
            g.add_edge(i, j)

    return g

def main():
    size = 10
    edge_probability = 0.25

    g = generate_random_graph(size, edge_probability)

    print("\n".join([ ",".join([ "1" if cell else "0" for cell in row ]) for row in g.adj ]))

    brute_force_solution = brute_force(g)

    print("brute_force", brute_force_solution)

    least_degree_solution = least_degree(g)

    print("least_degree", least_degree_solution)

    greatest_degree_solution = greatest_degree(g)

    print("greatest_degree", greatest_degree_solution)

if __name__ == "__main__":
    main()