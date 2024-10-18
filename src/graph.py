class Graph:
    def __init__(self, size: int, adj: list[list[bool]]):
        super().__init__()
        self.size = size
        self.adj = adj
    
    def add_edge(self, i: int, j: int):
        if i > j:
            self.add_edge(j, i)
        else:
            self.adj[i][j] = True
    
    def remove_edge(self, i: int, j: int):
        if i > j:
            self.remove_edge(j, i)
        else:
            self.adj[i][j] = False
    
    def has_edge(self, i: int, j: int):
        if i > j:
            return self.has_edge(j, i)
        else:
            return self.adj[i][j]

    def get_edges(self, i: int):
        return [idx for idx, is_edge in enumerate(self.adj[i]) if is_edge]
    
    def get_degree(self, i: int):
        return sum(self.adj[i])