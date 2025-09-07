import time
import numpy as np
import matplotlib.pyplot as plt

def execution_time(func, data, searching):
    start_time = time.perf_counter()
    func(data, searching)
    end_time = time.perf_counter()
    return (end_time - start_time)

def in_set(my_set, searching):
    return searching in my_set

def in_list(my_list, searching):
    return searching in my_list

rng = np.random.default_rng()
lists_count = 50
data_sizes = rng.integers(10, 10**5, size=lists_count).tolist()

random_numbers_lists = [rng.integers(low=0, high=10**6, size=size).tolist() for size in data_sizes]
random_sets = [set(number_list) for number_list in random_numbers_lists]

searchings = []
for i in range(lists_count):
    if rng.random() > 0.5:
        searchings.append(rng.choice(random_numbers_lists[i]))
    else:
        searchings.append(-10) # отрицательных чисел в списках нет

x_axis_data = data_sizes
y_axis_time_set = []
y_axis_time_list = []

for i in range(lists_count):
    timing1 = execution_time(in_list, random_numbers_lists[i], searchings[i])
    y_axis_time_list.append(timing1)
    
    timing2 = execution_time(in_set, random_sets[i], searchings[i])
    y_axis_time_set.append(timing2)

# график:
plt.xlabel('Размер данных')
plt.ylabel('Время')
plt.title('in для словарей и множеств')
plt.plot(x_axis_data, y_axis_time_set, color='blue', marker='o', markersize=7, label='множества')
plt.plot(x_axis_data, y_axis_time_list, color='green', marker='o', markersize=7, label='списки')
plt.legend()
plt.show()