import numpy as np


class MatrixInversionElementaryRowOperations:
    matrix = []

    def __init__(self, _matrix):
        self.matrix = []
        for i in range(len(_matrix)):
            self.matrix.append(np.append(_matrix[i], MatrixInversionElementaryRowOperations.get_one(i, len(_matrix[i]))))
        self.matrix = np.asarray(self.matrix)

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
        self.matrix[eliminating_row] -= self.matrix[row]*self.matrix[eliminating_row][row]/self.matrix[row][row]
        return

    def forward(self):
        row = len(self.matrix)
        for current_row in range(row-1):
            for eliminating_row in range(current_row+1, row):
                self.eliminate(current_row, eliminating_row)
        return

    def one(self):
        for i in range(len(self.matrix)):
            self.matrix[i] /= self.matrix[i][i]

    def backward(self):
        for i in reversed(range(len(self.matrix))):
            for j in reversed(range(i)):
                self.matrix[j] -= self.matrix[i]*self.matrix[j][i]

    def solve(self):
        self.forward()
        self.one()
        self.backward()
        return self.matrix[:, len(self.matrix):]


matrix = np.asarray([[25.0, 5.0, 1.0],
                     [64.0, 8.0, 1.0],
                     [144.0, 12.0, 1.0]])


print(np.linalg.inv(matrix))
print(MatrixInversionElementaryRowOperations(matrix).solve())
