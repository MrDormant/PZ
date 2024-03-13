import random
n = 3
# Создание списка из нескольких списков с рандомными числами
nested_list = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

print(nested_list)