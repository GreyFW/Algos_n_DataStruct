import time
import numpy as np
import matplotlib.pyplot as plt

def execution_time(func, data):
    data_copy = data.copy()
    start_time = time.perf_counter()
    func(data_copy)
    end_time = time.perf_counter()
    return (end_time - start_time)

def del_dict(my_dict):
    keys = list(my_dict.keys())
    for key in keys:
        del my_dict[key]

def del_list(my_list):
    for i in range(len(my_list) -1, -1, -1):
        # с конца по конец задом наперёд, избегаем проблемы подвижки индексов
        # за счёт сборщика мусора
        del my_list[i]

rng = np.random.default_rng()
lists_count = 50
data_sizes = rng.integers(10, 10**5, size=lists_count).tolist()

random_numbers_lists = [rng.integers(low=0, high=10**6, size=size).tolist() for size in data_sizes]

random_dictionatries = []
for size in data_sizes:
    keys = list(range(size)) # создаём список чисел диапазона, "как отрезок"
    values = rng.integers(low=0, high=10**6, size=size).tolist()
    # ^-- по каждому ключу лежит массив размера ключа с рандомными значениями
    new_dict = dict(zip(keys, values))
    random_dictionatries.append(new_dict)  

x_axis_data = data_sizes
y_axis_time_dict = []
y_axis_time_list = []

for i in range(lists_count):
    timing1 = execution_time(del_list, random_numbers_lists[i])
    y_axis_time_list.append(timing1)
    
    timing2 = execution_time(del_dict, random_dictionatries[i])
    y_axis_time_dict.append(timing2)

# график:
plt.xlabel('Размер данных')
plt.ylabel('Время')
plt.title('del для словарей и списков')
plt.plot(x_axis_data, y_axis_time_dict, color='blue', marker='o', markersize=7, label='словари')
plt.plot(x_axis_data, y_axis_time_list, color='green', marker='o', markersize=7, label='списки')
plt.legend()
plt.show()