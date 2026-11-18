import numpy as np

#Задание 1.

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

#Задание 2.

print("\nЗадание 2")

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

#Задание 3.

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("\nЗадание 3")

print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)

print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])

print("Центральный фрагмент 2x2:")
print(temperatures[:2, 1:3])

#Задание 4.

matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Исходная матрица:")
print(matrix)

part1 = matrix[:3, :]
print("Первые три строки:")
print(part1)
print("shape:", part1.shape)

part2 = matrix[-2:, :]
print("Последние две строки:")
print(part2)
print("shape:", part2.shape)

part3 = matrix[:, :2]
print("Первые два столбца:")
print(part3)
print("shape:", part3.shape)

part4 = matrix[1:4, 2:5]
print("Фрагмент строк 1-3 и столбцов 2-4:")
print(part4)
print("shape:", part4.shape)

part5 = matrix[-2:, -2:]
print("Правый нижний блок 2x2:")
print(part5)
print("shape:", part5.shape)