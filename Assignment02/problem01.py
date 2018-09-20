import numpy as np
import Assignment02.Equation as eq


class Problem01:
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
        return det_i / det


eps = pow(10, -10)
file = open(input('Enter file name: ')).readlines()
matrix = eq.Equation(file).get_matrix()
keys = matrix[1]
matrix = matrix[0]
p = Problem01(matrix)
out = open('out.txt', 'w')
for i in range(len(keys)):
    if float(p.solve(i)) < eps:
        out.write(str(keys[i]) + ' : ' + str(float(0))+'\n')
    else:
        out.write(str(keys[i]) + ' : ' + str(float(p.solve(i)))+'\n')
