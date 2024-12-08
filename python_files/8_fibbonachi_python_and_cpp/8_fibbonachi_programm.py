"""
Код восьмого способа нахождения чисел фибоначчи.
Основная логика программы будет написана на Python, также у нас будет происходить инициализация пула процессов, каждый из процессов для нахождения числа фибоначчи будет использовать код функции написанный на C++ при помощи shared object  (общих файлов)
"""

from multiprocessing import Pool
from ctypes import c_int64, CDLL
import time
import os
from utils import add_relative_import, error_cpp_not_found
add_relative_import()
from fib_settings import ACTIVATE_PROCESS_COUNT, MAX_FIB_NUMBER


OS_NAME = os.name

if OS_NAME == "nt":
    from ctypes import WinDLL

cpp_library = None

# Если пользователь запустил с Windows
if OS_NAME == "nt":
    
    try:
        # Делаем подключение динамической библиотеки
        cpp_library = WinDLL("library_files\\windows_library_fib.dll", winmode=0)
    except FileNotFoundError as Error:
        print(f"Файл динамической библиотеки Windows не найден, ошибка: {Error}")

# Если пользователь запустил с Linux
elif OS_NAME == "posix":
    
    try:
        cpp_library = CDLL("library_files/linux_fib_library.so")
    except FileNotFoundError as Error:
        print(f"Файл общего объекта для подключения не найден, ошибка: {Error}")

if not OS_NAME or not cpp_library:
    raise error_cpp_not_found



def fibbonachi(number: int):
    """
    Функция для вычисления чисел фибоначчи, по факту будет делать вызов функции, которая была написана на языке C++
    """
    
    # Переводим наше исходное число типа int, в тип int64, который нужен для нашей программы на C++
    number_int64 = c_int64(number)

    # Делаем обращение к нашему объекту библиотеки, вызываем оттуда функцию и передаем наше число
    fib_number_int64: c_int64 = cpp_library.fibbonachi_comp(number_int64)

    # Преобразование числа int64 в обычный int
    fib_number = int(fib_number_int64)
    return fib_number

def main():
    """Главная функция программы"""

    tasks_list = []

    # Делаем перебор от 0 до максимального числа, для которого нужно найти число фибоначчи
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_list.append(one_number_task)
    
    start_time = time.time()

    # Делаем создание пула процессов, указывая количество процессов как константу
    with Pool(ACTIVATE_PROCESS_COUNT) as pool_object:
        results_map: map = pool_object.map(fibbonachi, tasks_list)
        results_list: list = list(results_map)

    end_time = time.time()

    print(f"Все вычисления заняли: {end_time - start_time} секунд")
    print(results_list)

if __name__ == "__main__":
    main()

"""
Результат:
Все вычисления заняли: 3.093513011932373 секунд
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""