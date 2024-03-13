#В матрице элементы последнего столбца заменить на -1.

import random
from random import randint

n = int(input("введите размерность табльцы  "))
num = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
print("начальная табл ", num)
num = [y[:-1] + [-1] for y in num]
print(num)
