import numpy as np
import Assignment03.Equation as eq


class Problem01:
    matrix = []
    c = []
    keys = []
    lower = []
    upper = []

    def __init__(self, _matrix):
        _matrix, self.keys = _matrix
        if len(_matrix[0]) != len(_matrix) + 1:
            print('Invalid Matrix')
            exit(0)
        self.c = _matrix[:, len(_matrix):]
        _matrix = _matrix[:, 0:len(_matrix)]
        self.matrix = np.asarray(_matrix)
        self.lower = np.identity(len(self.matrix),float)
        print(self.matrix,self.c,self.keys)

    def eliminate(self, row, eliminating_row):
        if self.matrix[row][row] == 0:
            raise ValueError("division by zero")
        print('row[', eliminating_row, '] -= row[', row, '] *',
              self.matrix[eliminating_row][row] / self.matrix[row][row])
        self.lower[eliminating_row][row] = self.matrix[eliminating_row][row] / self.matrix[row][row]
        self.matrix[eliminating_row] -= self.matrix[row] * self.matrix[eliminating_row][row] / self.matrix[row][row]
        print('Upper: ')
        print(self.matrix)
        print('Lower: ')
        print(self.lower)
        return

    def forward(self):
        row = len(self.matrix)
        for current_row in range(row - 1):
            for eliminating_row in range(current_row + 1, row):
                self.eliminate(current_row, eliminating_row)
        return

    def decompose(self):
        self.forward()
        self.upper = self.matrix
        print('----------Decompose done----------')

    def solve(self):
        self.decompose()
        print('Z')
        z = np.dot(np.linalg.inv(p.lower),p.c)
        print(z)
        ret = np.dot(np.linalg.inv(p.upper),z)
        print('solve')
        print(ret)
        return ret


eps = pow(10, -10)
file = open(input('Enter file name: ')).readlines()
matrix = eq.Equation(file).get_matrix()
p = Problem01(matrix)
solve = p.solve()
out = open('out.txt', 'w')
for i in range(len(p.keys)):
    if -eps < float(solve[i]) < eps:
        out.write(str(p.keys[i]) + ' : ' + str(float(0))+'\n')
    else:
        out.write(str(p.keys[i]) + ' : ' + str(float(solve[i]))+'\n')
