import numpy as np
import Assignment02.Equation as eq


class Problem01:
    matrix = []
    c = []

    def __init__(self, _matrix):
        self.c = _matrix[:, len(_matrix):].flatten()
        self.matrix = _matrix[:, 0:len(_matrix)]

    @staticmethod
    def det(_matrix):
        if len(_matrix) == 1:
            return _matrix[0][0]
        result = 0.0
        for i in range(len(_matrix)):
            temp = np.copy(np.concatenate((_matrix[1:, 0:i], _matrix[1:, i + 1:]), axis=1))
            result += pow(-1, i) * Problem01.det(temp) * _matrix[0][i]
        return result

    def solve(self, i):
        det = Problem01.det(self.matrix)
        mat_i = np.copy(self.matrix)
        mat_i[:, i] = self.c
        print(i, ":")
        print(mat_i)
        det_i = Problem01.det(mat_i)
        return det_i / det


eps = pow(10, -10)
file = open(input('Enter file name: ')).readlines()
matrix = eq.Equation(file).get_matrix()
keys = matrix[1]
matrix = matrix[0]
print(matrix)
p = Problem01(matrix)
out = open('out.txt', 'w')
for i in range(len(keys)):
    solve = p.solve(i)
    if -eps < float(solve) < eps:
        out.write(str(keys[i]) + ' : ' + str(float(0))+'\n')
    else:
        out.write(str(keys[i]) + ' : ' + str(float(solve))+'\n')
