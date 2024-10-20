from src.graph import Graph
from src.zero_force import zero_force
from src.powerset import powerset_under_k

def k_subsets(g: Graph, k: int):
    return k_subsets_recursive(g, k, set(), set())

def k_subsets_recursive(g: Graph, k: int, colored_set: set[int], forced_set: set[int]):
    available_vertices = [i for i in range(g.size) if i not in forced_set]

    best_colored_set = colored_set
    best_forced_set = set()
    best_forcing_size = len(forced_set)

    for candidate_new_colorings in powerset_under_k(available_vertices, k):
        candidate_forced_set = zero_force(g, forced_set.union(candidate_new_colorings))
        candidate_forcing_size = len(candidate_forced_set)

        candidate_colored_set = colored_set.union(candidate_new_colorings)

        # if we have colored all the nodes, simply return
        if candidate_forcing_size == g.size:
            return candidate_colored_set

        # if we have made at least a new PR, then save it
        elif candidate_forcing_size > best_forcing_size:
            best_forcing_size = len(candidate_forced_set)
            best_colored_set = candidate_colored_set
            best_forced_set = candidate_forced_set

    return k_subsets_recursive(g, k, best_colored_set, best_forced_set)