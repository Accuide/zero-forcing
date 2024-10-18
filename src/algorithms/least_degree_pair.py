from src.graph import Graph
from src.zero_force import zero_force

def least_degree_pair(g: Graph) -> set[int]:
    non_zero_nodes = list(filter(lambda i: g.get_degree(i) > 0, range(0, g.size)))

    if len(non_zero_nodes) == 0:
        return set()
    
    pair = min([(a, b) for a in non_zero_nodes for b in non_zero_nodes if a != b], key=lambda pair: g.get_degree(pair[0]) + g.get_degree(pair[1]))

    forced = zero_force(g, { pair[0], pair[1] })

    g_clone = g.clone()
    
    for j in forced:
        g_clone.remove_all_edges(j)
    
    return least_degree_pair(g_clone).union(forced)