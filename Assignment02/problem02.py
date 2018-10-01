import numpy as np
import Assignment02.Equation as eq


class Problem02:
    matrix = []
    c = []

    def __init__(self, _matrix):
        self.c = _matrix[:, len(_matrix):]
        _matrix = _matrix[:, 0:len(_matrix)]
        self.matrix = []
        for i in range(len(_matrix)):
            self.matrix.append(np.append(_matrix[i], Problem02.get_one(i, len(_matrix[i]))))
        self.matrix = np.asarray(self.matrix)
        print(self.matrix)

    @staticmethod
    def get_one(i, n):
        result = [0.0 for j in range(n)]
        result[i] = 1.0
        return np.asarray(result)

    @staticmethod
    def scan_matrix():
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        mat = []
        for i in range(row):
            row = []
            for j in range(col):
                row.append(float(input()))
            mat.append(row)
        return np.asarray(mat)

    @staticmethod
    def swap_row(mat, i, j):
        mat[[i, j]] = mat[[j, i]]
        return mat

    def eliminate(self, row, eliminating_row):
        if self.matrix[row][row] == 0:
            raise ValueError("division by zero")
        print('row', eliminating_row, '-= row', row, '*', self.matrix[eliminating_row][row]/self.matrix[row][row])
        self.matrix[eliminating_row] -= self.matrix[row]*self.matrix[eliminating_row][row]/self.matrix[row][row]
        print(self.matrix)
        return

    def forward(self):
        row = len(self.matrix)
        for current_row in range(row-1):
            for eliminating_row in range(current_row+1, row):
                self.eliminate(current_row, eliminating_row)
        return

    def one(self):
        for i in range(len(self.matrix)):
            print("row", i, "/=", self.matrix[i][i])
            self.matrix[i] /= self.matrix[i][i]
            print(self.matrix)

    def backward(self):
        for i in reversed(range(len(self.matrix))):
            for j in reversed(range(i)):
                print('row', j, '-= row', i, '*',self.matrix[j][i])
                self.matrix[j] -= self.matrix[i]*self.matrix[j][i]
                print(self.matrix)

    def inverse(self):
        self.forward()
        self.one()
        self.backward()
        return self.matrix[:, len(self.matrix):]


eps = pow(10, -10)
file = open(input('Enter file name: ')).readlines()
matrix = eq.Equation(file).get_matrix()
keys = matrix[1]
matrix = matrix[0]
print(matrix)
p = Problem02(matrix)
solve = np.dot(p.inverse(), p.c)
out = open('out.txt', 'w')
for i in range(len(keys)):
    if -eps < float(solve[i]) < eps:
        out.write(str(keys[i]) + ' : ' + str(float(0))+'\n')
    else:
        out.write(str(keys[i]) + ' : ' + str(float(solve[i]))+'\n')
