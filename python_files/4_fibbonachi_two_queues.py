"""
Код четвертого способа вычисления чисел Фибоначчи.
Использование двух очередей, одна очередь будет использоваться под задачи, вторая очередь под результаты вычислений, процессов опять же будет ограниченное количество, поэтому будет создан цикл внутри процесса, процесс должен будеть работать до тех пор, пока очередь задач не пуста
"""

from fib_settings import MAX_FIB_NUMBER, ACTIVATE_PROCESS_COUNT
from multiprocessing import Process, Queue
import time

def worker_process_func(tasks_queue: Queue, results_queue: Queue) -> None:
    """Функция, которая будет выполняться каждым отдельным процессом"""
    def fibbonachi(number: int) -> int:
        """Функция, для высчитывания числа фибоначчи рекурсивным образом"""
        if number == 0:
            return 0
    
        if number < 2:
            return 1

        fib_number: int = fibbonachi(number - 2) + fibbonachi(number - 1)
        return fib_number
    
    # Процесс будет работать до тех пор, пока очередь задач не пуста
    while not tasks_queue.empty():
        # Делаем получение числа из очереди задач, после находим число фибоначчи, после чего помещаем полученное число в очередь результатов

        one_number_task = tasks_queue.get()
        fib_number = fibbonachi(one_number_task)
        results_queue.put(fib_number)


def main():
    """Главная функция, где лежит логика программы"""
    tasks_queue: Queue = Queue()
    results_queue: Queue = Queue()

    # Делаем перебор от 0 до максимального числа, от которого мы хотим получить число фибоначчи и помещаем числа в очередь задач
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_queue.put(one_number_task)
    
    process_list = []

    started_time = time.time()

    # Делаем создание определенного количества процессов, указывая как параметры очереди задач и результатов, помещая объект процесса в список процессов
    for index_process in range(0, ACTIVATE_PROCESS_COUNT):
        process_object: Process = Process(target=worker_process_func, args=(tasks_queue, results_queue,))
        process_list.append(process_object)

    # Делаем перебор списка процессов и запускаем каждый процесс
    for one_process in process_list:
        one_process.start()


    # Делаем перебор списка процессов и делаем слияние каждого процесса с главным процессом, то есть ожидаем, когда каждый процесс завершит свою работу
    for one_process in process_list:
        one_process.join()

    
    end_time = time.time()

    print(f"Время всех вычислений: {end_time - started_time} секунд")

    results_list = []
    
    for index in range(0, MAX_FIB_NUMBER+1):
        fib_number = results_queue.get()
        results_list.append(fib_number)

    print(results_list)
    print("После сортировки:")
    print(sorted(results_list))


# Если файл запущен из консоли
if __name__ == "__main__":
    main()

"""
Результат:
Время всех вычислений: 89.24480843544006 секунд
[0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 1597, 4181, 10946, 28657, 1, 75025, 987, 2584, 6765, 17711, 46368, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
После сортировки:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""