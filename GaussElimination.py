import numpy as np
class GaussElimination:
    matrix = []

    def __init__(self, _matrix):
        self.matrix = _matrix

    @staticmethod
    def scan_matrix():
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        mat = []
        for i in range(row):
            row=[]
            for j in range(col):
                row.append(float(input()))
            mat.append(row)
        return np.asarray(mat)

    @staticmethod
    def swap_row(mat, i, j):
        mat[[i, j]]=mat[[j, i]]
        return mat

    def eliminate(self, row, eliminating_row):
        if self.matrix[row][row] == 0:
            raise ValueError("division by zero")
        self.matrix[eliminating_row] -= self.matrix[row]*self.matrix[eliminating_row][row]/self.matrix[row][row]
        return

    def forward(self, partial_pivoting=None):
        if len(self.matrix) != len(self.matrix[0]) - 1:
            print("No unique solution")
            return
        row = len(self.matrix)
        for current_row in range(row-1):
            if partial_pivoting is not None:
                max_row = current_row
                for i in range(current_row,row):
                    if self.matrix[i][current_row]>self.matrix[max_row][current_row]:
                        max_row = i
                self.matrix = GaussElimination.swap_row(self.matrix, current_row, max_row)
            for eliminating_row in range(current_row+1,row):
                self.eliminate(current_row, eliminating_row)
        return

    def backward(self):
        row = len(self.matrix)
        solve  = [0.0 for i in range(row)]
        for i in reversed(range(row)):
            if self.matrix[i][i]==0:
                raise ValueError('No unique solution')
            for j in range(i+1, row):
                solve[i] -= self.matrix[i][j]*solve[j]
            solve[i] += self.matrix[i][row]
            solve[i] /= self.matrix[i][i]
        return solve

    def solve(self, partial_pivoting=None):
        self.forward(partial_pivoting)
        return self.backward()

    def predict(self, parameters):
        solve = self.solve()
        if len(solve) != len(parameters):
            raise ValueError('Invalid parameters')
        return np.dot(np.asarray(solve),np.asarray(parameters))


matrix = np.asarray([[25.0, 5.0, 1.0, 106.8],
                     [64.0, 8.0, 1.0, 177.2],
                     [144.0, 12.0, 1.0, 279.2]])

g = GaussElimination(matrix)
print(g.solve())
print(g.predict([25.0, 5.0, 1.0]))
