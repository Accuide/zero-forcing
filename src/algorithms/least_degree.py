from src.graph import Graph
from src.zero_force import zero_force

def least_degree(g: Graph) -> set[int]:
    """
    1. Choose node of least degree
    2. Color it
    3. Run zero forcing
    4. Remove all those nodes from the graph
    5. Repeat
    """
    non_zero_nodes = list(filter(lambda i: g.get_degree(i) > 0, range(0, g.size)))
    
    if len(non_zero_nodes) == 0:
        return set()
    
    i = min(*non_zero_nodes, key=g.get_degree)

    forced = zero_force(g, { i })

    g_clone = g.clone()
    
    for j in forced:
        g_clone.remove_all_edges(j)
    
    return least_degree(g_clone).union(forced)