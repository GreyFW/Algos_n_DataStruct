import numpy as np
import time
import matplotlib.pyplot as plt

"""
Сложность -- O(n)
Хорошая оптимизация за счёт того что все ф-ции == встроенные
"""
def solution1(random_numbers):
    numbers = random_numbers.copy()
    max1 = max(numbers)
    max1_index = numbers.index(max1)
    numbers.pop(max1_index)
    
    numbers = random_numbers.copy()
    max2 = max(numbers)
    max2_index = numbers.index(max2)
    numbers.pop(max2_index)
    
    numbers = random_numbers.copy()
    max3 = max(numbers)
    
    return max1, max2, max3

"""
Сложность -- O(n)
Но работает медленнее первого, т.к. не использует встроенные
функции поиска, оптимизированные разработчиками языка
"""
def solution2(random_numbers):
    numbers = random_numbers.copy()
    max_values = []
    for _ in range(3):
        current_max = 0
        max_index = -1
        for i in range(len(numbers)):
            if numbers[i] > current_max:
                current_max = numbers[i]
                max_index = i
        max_values.append(current_max)
        numbers.pop(max_index)
    return tuple(max_values)

def execution_time(func, data):
    data_copy = data.copy()
    start_time = time.perf_counter()
    func(data_copy)
    end_time = time.perf_counter()
    return (end_time - start_time)

rng = np.random.default_rng()
lists_count = 50
data_sizes = rng.integers(10, 10**5, size=lists_count).tolist()
# ^-- ось х, храним размеры списков чисел

random_numbers_lists = [rng.integers(low=0, high=10**6, size=size).tolist() for size in data_sizes]
 
y_solution1 = [] # ось у, время 1го реш-я
y_solution2 = [] # ось у, время 2го реш-я
    
# собрали все данные, теперь вычислим координаты по у для обоих реш.

for numbers_list in random_numbers_lists:
    timing1 = execution_time(solution1, numbers_list)
    y_solution1.append(timing1)
    
    timing2 = execution_time(solution2, numbers_list)
    y_solution2.append(timing2)

# график:
plt.xlabel('кол-во чисел')
plt.ylabel('Время')
plt.title('Время выполнения в зависимости от кол-ва символов')
plt.plot(data_sizes, y_solution1, color='blue', marker='o', markersize=7, label='1е реш')
plt.plot(data_sizes, y_solution2, color='green', marker='o', markersize=7, label='2е реш')
plt.legend()
plt.show()