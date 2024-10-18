import numpy as np

class Graph:
    def __init__(self, size: int, adj: np.ndarray):
        super().__init__()
        self.size = size
        self.adj = adj