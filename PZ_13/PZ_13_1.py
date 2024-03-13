"""В матрице элементы строки N (N задать с клавиатуры) увеличить на 3."""
import random
from random import randint

n = int(input("введите размерность табльцы  "))
num = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
print("начальная табл ", num)
table = [y[:-1] + [y[-1] + 3] for y in num]
print("конечная табл ", table)
