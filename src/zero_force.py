from src.graph import Graph

def zero_force(g: Graph, initial: set[int]) -> set[int]:
    forced_set = { i for i in initial }
    queue = [ i for i in initial ]
    
    iterations_since_changed = 0

    while len(queue) > 0 and iterations_since_changed < g.size:
        i = queue.pop(0)
        total_nodes = 0
        forced_nodes = 0
        last_unforced_node = 0
        for j in [idx for idx, is_edge in enumerate(g.adj[i]) if is_edge]:
            total_nodes += 1
            if j in forced_set:
                forced_nodes += 1
            else:
                last_unforced_node = j
        if forced_nodes == total_nodes - 1:
            forced_set.add(last_unforced_node)
            queue.append(last_unforced_node)
            iterations_since_changed = 0
        else:
            queue.append(i)
            iterations_since_changed += 1

    return forced_set