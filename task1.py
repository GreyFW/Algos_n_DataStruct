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
def foo(s):
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

import time

def execution_time(data):
    start_time = time.perf_counter()
    foo(data)
    end_time = time.perf_counter()
    return (end_time - start_time)

def string_generation():
    

