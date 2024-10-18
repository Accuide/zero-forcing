from src.graph import Graph
from src.zero_force import zero_force

def leaf_search(g: Graph) -> set[int]:

    all_leaves = [ i for i in range(g.size) if g.get_degree(i) == 1 ]

    if len(all_leaves) == 0:
        pass
    else:
        # pick a leaf
        i = all_leaves[0]
        root = g.get_edges(i)[0]
        other_leaves = [j for j in g.get_edges(root) if j != i and g.get_degree(j) == 1]
        forced = zero_force(g, { i, *other_leaves })
        g_clone = g.clone()
        for j in forced:
            g_clone.remove_all_edges(j)
        return leaf_search(g_clone).union({ i, *other_leaves })