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
    non_zero_nodes = [ i for i in range(g.size) if g.get_degree(i) > 0 ]
    
    if len(non_zero_nodes) == 0:
        return set()
    
    initial_set = { min(*non_zero_nodes, key=g.get_degree) }

    forced = zero_force(g, initial_set)

    leftover_leaves = [ i for i in non_zero_nodes if i not in forced and g.get_degree(i) == 1 and g.get_edges(i)[0] in forced]
    leftover_leaf_groups = { k: [ i for i in g.get_edges(k) if i not in forced ] for k in { g.get_edges(i)[0] for i in leftover_leaves } }
    
    for parent in leftover_leaf_groups:
        for rel_idx, i in enumerate(leftover_leaf_groups[parent]):
            forced.add(i)
            if rel_idx != 0:
                initial_set.add(i)

    g_clone = g.clone()
    
    for j in forced:
        g_clone.remove_all_edges(j)
    
    return least_degree(g_clone).union(initial_set)