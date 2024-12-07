"""
Код восьмого способа нахождения чисел фибоначчи.
Основная логика программы будет написана на Python, также у нас будет происходить инициализация пула процессов, каждый из процессов для нахождения числа фибоначчи будет использовать код функции написанный на C++ при помощи shared object  (общих файлов)
"""

from multiprocessing import Pool
from ctypes import c_int64, CDLL, WinDLL
import time
import os
from utils import add_relative_import, error_cpp_not_found
add_relative_import()
from fib_settings import ACTIVATE_PROCESS_COUNT, MAX_FIB_NUMBER


OS_NAME = os.name

cpp_library = None

# Если пользователь запустил с Windows
if OS_NAME == "nt":
    
    try:
        # Делаем подключение динамической библиотеки
        cpp_library = WinDLL("windows_fibbonachi_library.dll", winmode=0)
    except FileNotFoundError as Error:
        print(f"Файл динамической библиотеки Windows не найден, ошибка: {Error}")

# Если пользователь запустил с Linux
elif OS_NAME == "posix":
    
    try:
        cpp_library = CDLL("./linux_fibbonachi_library.so")
    except FileNotFoundError as Error:
        print(f"Файл общего объекта для подключения не найден, ошибка: {Error}")

if not OS_NAME or not cpp_library:
    raise error_cpp_not_found



def fibbonachi(number: int):
    """Функция для вычисления чисел фибоначчи, по факту будет делать вызов функции, которая была написана на языке C++"""
    pass