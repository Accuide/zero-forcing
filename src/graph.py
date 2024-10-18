class Graph:
    def __init__(self, size: int, adj: list[list[bool]]):
        super().__init__()
        self.size = size
        self.adj = adj