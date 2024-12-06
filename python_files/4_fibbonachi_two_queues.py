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
    pass