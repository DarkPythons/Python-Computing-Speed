"""
Код первого способа вычисления чисел Фибоначчи. 
Использование лишь рекурсии, без какого-либо кэша.
"""

import time
from fib_settings import MAX_FIB_NUMBER


def fibbonachi(number: int) -> int:
    """Функция для вычисления чисел Фибоначчи рекурсивным способом"""
    
    if number == 0:
        return 0

    if number < 2:
        return 1
    
    number_fib = fibbonachi(number - 1) + fibbonachi(number - 2)
    return number_fib

def main():
    """Главная функция со всей логикой программы"""
    tasks_list = []

    # Создание списка задач
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_list.append(one_number_task)

    fibbonachi_list = []
    
    started_time = time.time()

    for index in range(0, MAX_FIB_NUMBER+1):
        number = tasks_list[0]
        fibbonachi_number: int = fibbonachi(number)
        del tasks_list[0]

        # Делаем добавление вычисленного числа фибоначчи в список чисел фибоначчи
        fibbonachi_list.append(fibbonachi_number)

    end_time = time.time()

    print(f"Время всех вычислений: {end_time - started_time} секунд")
    print(fibbonachi_list)

# Если файл запустили из консоли
if __name__ == "__main__":
    main()

"""
Результат: 
Время всех вычислений: 140.3150246143341 секунд
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""