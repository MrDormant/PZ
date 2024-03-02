"""В матрице элементы строки N (N задать с клавиатуры) увеличить на 3."""

import numpy as np
N = int(input("Введите число N: "))
matrix = np.random.randint(1, 10, size=(N, N))
print(matrix)
matrix[N - 1, :] += 3
print(matrix)
