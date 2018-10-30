import math

import numpy as np
import GaussSeidal.Equation as eq


class Problem01:
    matrix = []
    c = []
    keys = []
    solution = []

    def __init__(self, _matrix):
        _matrix, self.keys = _matrix
        if len(_matrix[0]) != len(_matrix) + 1:
            print('Invalid Matrix')
            exit(0)
        self.c = _matrix[:, len(_matrix):]
        _matrix = _matrix[:, 0:len(_matrix)]
        self.matrix = np.asarray(_matrix)
        self.solution = [0.0 for i in range(len(self.matrix))]
        self.check_dominant()
        print(self.matrix, self.c, self.keys, self.solution)

    def check_dominant(self):
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            diag = math.fabs(row[i])
            sum = 0.0
            for j in range(len(row)):
                if j != i:
                    sum += math.fabs(row[j])
            if sum > diag:
                raise ValueError("Not Diagonal Dominant")

    def solve(self, i):
        ans = self.c[i][0]
        ans -= np.dot(self.matrix[i], self.solution)
        ans += self.matrix[i][i] * self.solution[i]
        ans /= self.matrix[i][i]
        return ans

    def run(self, iterations):
        for i in range(iterations):
            for j in range(len(self.solution)):
                self.solution[j] = self.solve(j)
                print(self.solution)
            print('------------------------------')


eps = pow(10, -10)
# file = open(input('Enter file name: ')).readlines()
file = open('in2.txt').readlines()
matrix = eq.Equation(file).get_matrix()
p = Problem01(matrix)
p.run(1000)
solve = p.solution

out = open('out.txt', 'w')
for i in range(len(p.keys)):
    if -eps < float(solve[i]) < eps:
        out.write(str(p.keys[i]) + ' : ' + str(float(0))+'\n')
    else:
        out.write(str(p.keys[i]) + ' : ' + str(float(solve[i]))+'\n')