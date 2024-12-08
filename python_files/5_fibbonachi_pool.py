"""
Код пятого способа вычисления чисел Фибоначчи.
Использование Pool объекта, который будет создавать набор (кластер) процессов, который и будет 
вычислять наши числа.
"""

from multiprocessing import Pool
from fib_settings import ACTIVATE_PROCESS_COUNT, MAX_FIB_NUMBER
import time


def fibbonachi(number: int) -> int:
    """Функция для вычисления чисел фибоначчи рекурсивным способом"""
    if number == 0:
        return 0
    
    if number < 2:
        return 1
    
    fib_number = fibbonachi(number - 2) + fibbonachi(number - 1)
    return fib_number

def main():
    """Главная функция, которая содержит всю логику программы"""

    tasks_list = []

    # Делаем перебор от 0 до максимального числа, для которого нужно будет вычислить число 
    # фибоначчи, помещая все числа в список задач
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_list.append(one_number_task)

    start_time = time.time()

    # Делаем создание пула процессов, указывая какое количество процессов нам нужно
    with Pool(ACTIVATE_PROCESS_COUNT) as pool_object:
        result_map = pool_object.map(fibbonachi, tasks_list)
        result_list = list(result_map)

    end_time = time.time()

    print(f"Все вычисления заняли: {end_time - start_time} секунд")
    print(result_list)


# Если программа запущена из консоли
if __name__ == "__main__":
    main()

"""
Результат:
Все вычисления заняли: 70.81541061401367 секунд
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 
17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 
5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""
