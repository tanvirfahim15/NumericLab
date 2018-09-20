import numpy as np

matrix = np.asarray([[25.0, 5.0, 1.0],
                     [64.0, 8.0, 1.0],
                     [144.0, 12.0, 1.0]])


def det(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0.0
    for i in range(len(matrix)):
        temp = np.copy(np.concatenate((matrix[1:, 0:i], matrix[1:, i + 1:]), axis=1))
        print(temp)
        result += ((-1) ** i) * det(temp)
        print(det(temp))
    return result

print(det(matrix))