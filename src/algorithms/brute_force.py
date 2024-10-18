from src.graph import Graph
from src.zero_force import zero_force
from src.powerset import powerset

def brute_force(g: Graph) -> set[int]:
    """
    Runtime: O(2^n)
    """
    for initial_set in powerset(range(0, g.size)):
        if len(zero_force(g, initial_set)) == g.size:
            return initial_set