"""
Код девятого способа вычисления чисел фибоначчи
Использование кэширования. Так как мы используем рекурсию, у нас будет происходить вызов нашей функции множество раз с теми же параметрами, поэтому хорошим решением будет кэширование  
"""

from fib_settings import MAX_FIB_NUMBER
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibbonachi(number: int) -> int:
    """Функция для вычисления чисел фибоначчи"""
    if number == 0:
        return 0
    if number < 2:
        return 1
    
    fib_number = fibbonachi(number - 2) + fibbonachi(number - 1)
    return fib_number

def main():
    """Главная функция"""

    tasks_list = []

    # Делаем перебор от 0 до максимального числа для которого нужно найти число фибоначчи, пополняя список задач
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_list.append(one_number_task)

    results_list = []

    start_time = time.time()

    # Делаем вызов функции для нахождения числа фибоначчи от нашего числа, после помещаем число фибоначчи в список результатов
    for one_number_task in tasks_list:
        fib_number = fibbonachi(one_number_task)
        results_list.append(fib_number)

    end_time = time.time()

    print(f"Все вычисления заняли: {end_time - start_time} секунд")
    print(results_list)

if __name__ == "__main__":
    main()

"""
Результат:
Все вычисления заняли: 0.0 секунд
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""