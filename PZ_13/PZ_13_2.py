#В матрице элементы последнего столбца заменить на -1.

import numpy as np
N = int(input("Введите число N: "))
matrix = np.random.randint(1, 10, size=(N, N))
print(matrix)
matrix[:, -1] = -1
print(matrix)