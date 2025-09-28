""" 
1) Что выполняет приведенная функция? 
- Принимает строку;
- Затем проходится по каждому символу строки, проверяя,
является ли он цифрой. Если да, то добавляет в сумму.

Итого: возвращает сумму цифр строки.


2) Какова вычислительная сложность алгоритма (в О-нотации)?
- O(n)
- т.к. проходим цикл по элементам строки, при этом n == длина строки (в символах) 

"""

""" 3 вариант """

import time
import string
import random
import matplotlib.pyplot as plt

def foo(s):
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

def execution_time(data):
    start_time = time.perf_counter()
    foo(data)
    end_time = time.perf_counter()
    return (end_time - start_time)

def generate_random_string(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

max_length = 1000000 # 1 million
current_length = 10

random_strings = []
while current_length < max_length:
    random_strings.append(generate_random_string(current_length))
    current_length += 10000
# сгенерировали строки

execution_timings = []      # ось у
x_axis = []                 # ось х

for str in random_strings:
    x_axis.append(len(str))
# собрали длины строк, сорт. по возрастанию

for str in random_strings:
    timing = execution_time(str)
    execution_timings.append(timing)

# к этому моменту имеем данные для обеих осей; строим график

plt.xlabel('Символов')
plt.ylabel('Время')
plt.title('Время выполнения в зависимости от длины строки')
plt.plot(x_axis, execution_timings, color='blue', marker='o', markersize=7)
plt.show()