import numpy as np


class Cramer:
    matrix = []
    c = []

    def __init__(self, _matrix):
        self.c = _matrix[:, len(_matrix):].flatten()
        self.matrix = _matrix[:, 0:len(_matrix)]

    def solve(self, i):
        det = np.linalg.det(self.matrix)
        mat_i = np.copy(self.matrix)
        mat_i[:, i] = self.c
        det_i = np.linalg.det(mat_i)
        return det_i/det


matrix = np.asarray([[25.0, 5.0, 1.0, 106.8],
                     [64.0, 8.0, 1.0, 177.2],
                     [144.0, 12.0, 1.0, 279.2]])
c = Cramer(matrix)
for i in range(len(c.matrix)):
    print(c.solve(i))