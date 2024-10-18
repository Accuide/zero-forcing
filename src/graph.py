class Graph:
    def __init__(self, size: int, adj: list[list[bool]]):
        super().__init__()
        self.size = size
        self.adj = adj
    
    def add_edge(self, i: int, j: int):
        if i != j:
            self.adj[i][j] = True
            self.adj[j][i] = True
    
    def remove_edge(self, i: int, j: int):
        self.adj[i][j] = False
        self.adj[j][i] = False
    
    def remove_all_edges(self, i):
        for j in range(self.size):
            self.remove_edge(i, j)

    def has_edge(self, i: int, j: int):
        return self.adj[i][j]

    def get_edges(self, i: int):
        return [idx for idx, is_edge in enumerate(self.adj[i]) if is_edge]
    
    def get_degree(self, i: int):
        return sum(self.adj[i])
    
    def clone(self):
        return Graph(self.size, [[cell for cell in row] for row in self.adj])