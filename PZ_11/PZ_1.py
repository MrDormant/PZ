import random
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:
numbers = [random.randint(-100, 100) for _ in range(20)]

with open("../numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

num_elements = len(numbers)
avg_elements = sum(numbers) / num_elements
positive_even_numbers = [num for num in numbers if num > 0 and num % 2 == 0]
sum_positive_even = sum(positive_even_numbers)
avg_positive_even = sum_positive_even / len(positive_even_numbers)

# Записываем результаты в новый текстовый файл
with open("../output.txt", "w") as file:
    file.write("Исходные данные:\n")
    file.write(f"Количество элементов: {num_elements}\n")
    file.write(f"Среднее арифметическое элементов: {avg_elements:.2f}\n")
    file.write("Положительные четные элементы:\n")
    for num in positive_even_numbers:
        file.write(str(num) + "\n")
    file.write(f"Сумма положительных четных элементов: {sum_positive_even}\n")
    file.write(f"Среднее арифметическое положительных четных элементов: {avg_positive_even:.2f}\n")

print("Результаты записаны в файл 'output.txt'.")
