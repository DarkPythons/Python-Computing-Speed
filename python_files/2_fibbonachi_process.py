"""
Код второго способа вычисления чисел Фибоначчи. 
Использование того же алгоритма рекурсии, но теперь вычисление каждого числа будет происходить при помощи множества процессов, а точнее процессов будет столько же, сколько и задач
"""

from multiprocessing import Process, Manager
from multiprocessing.managers import ListProxy
import time
from fib_settings import MAX_FIB_NUMBER


def fibbonachi(number: int, shared_list_object: ListProxy = None) -> int:
    """Функция для вычисления чисел Фибоначчи рекурсивным способом"""
    
    if number == 0:
        return 0

    if number < 2:
        return 1
    
    number_fib = fibbonachi(number - 1) + fibbonachi(number - 2)


    # Нужно сделать проверку, есть ли у нас общий список между процессами, если там будет None, значит это просто функция, которая запущена рекурсивно, и делать добавление этого числа в результат не нужно
    # Делаем проверку именно на None, так изначально список пустой, а [] считается за False
    if shared_list_object != None:
        # Делаем помещение в общий объект списка между процессами нашего числа фибоначчи
        shared_list_object.append(number_fib)
    return number_fib

def main():
    """Главная функция со всей логикой программы"""
    tasks_list = []

    # Создаем общий объект списка результатов для того, чтобы процессы после высчитывания чисел фибоначчи, могли положить их туда, а мы после в главном процессе получить список результатов
    manager_object = Manager()
    results_lists = manager_object.list()

    # Делаем добавление первых чисел
    results_lists.append(0)
    results_lists.append(1)

    # Создание списка задач
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_list.append(one_number_task)

    process_list = []

    started_time = time.time()

    # Создание списка незапущенных, но уже инициализированных процессов (точнее объектов)
    for one_number_task in tasks_list:
        process_object = Process(target=fibbonachi, args=(one_number_task, results_lists, ))
        process_list.append(process_object)

    # В этом цикле будет происходить запуск всех процессов, которые начнут выполнять функцию, с переданным ей параметром ранее
    for one_process in process_list:
        one_process.start()

    # В этом цикле происходит слияние (присоединение) всех дочерних процессов к главному, и чтобы слияние произошло, нужно чтобы процесс завершил работу, поэтому ждем пока все процессы завершат вычисление
    for one_process in process_list:
        one_process.join()

    end_time = time.time()

    results_lists: list = list(results_lists)

    print(f"Время всех вычислений: {end_time - started_time} секунд")
    print(results_lists)
    print("После сортировки: ")
    print(sorted(results_lists))


# Если файл запустили из консоли
if __name__ == "__main__":
    main()

"""
Результат: 
Время всех вычислений: 103.90364742279053 секунд
[0, 1, 46368, 5, 1, 987, 10946, 3, 21, 17711, 610, 28657, 1597, 2584, 8, 377, 2, 34, 144, 55, 121393, 89, 196418, 6765, 317811, 13, 233, 514229, 4181, 832040, 75025, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
После сортировки:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""