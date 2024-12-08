"""
Код третьего способа вычисления чисел Фибоначчи. 
Использование одной очереди, которая будет содержать в себе задачи, каждый процесс, а процессов у 
нас будет ограниченное количество, будет брать себе задачу из этой очереди до тех пор, пока очередь 
не будет пустой
"""

from multiprocessing import Process, Manager, Queue
from multiprocessing.managers import ListProxy
from fib_settings import MAX_FIB_NUMBER, ACTIVATE_PROCESS_COUNT
import time

def worker_process_func(tasks_queue: Queue, shared_list_object: ListProxy = None) -> None:
    """Функция, которая будет выполняться каждым отдельным процессом"""

    def fibbonaci(number: int):
        """Функция для нахождения числа фибоначчи"""

        if number == 0:
            return 0
        
        if number < 2:
            return 1
        
        fib_number: int = fibbonaci(number - 2) + fibbonaci(number - 1)
        return fib_number
    
    # Процесс будет работать до тех пор, пока очередь задач полностью не опустеет
    while not tasks_queue.empty():
        one_number_task: int = tasks_queue.get()

        fib_number = fibbonaci(one_number_task)

        # В общий объект списка делаем добавление нашего результата (числа фибоначчи)
        shared_list_object.append(fib_number)

def main():
    # Делаем создание объекта очереди
    tasks_queue: Queue = Queue()

    # Делаем добавление в очередь задач чисел для которых нужно будет найти числа фибоначчи
    for one_number_task in range(0, MAX_FIB_NUMBER+1):
        tasks_queue.put(one_number_task)

    # Создаем общий объект списка результатов для того, чтобы процессы после высчитывания чисел 
    # фибоначчи, могли положить их туда, а мы после в главном процессе получить список результатов
    manager_object = Manager()
    shared_results_list = manager_object.list()


    process_list = []

    started_time = time.time()

    # Делаем создание списка процессов, указывая количество процессов как константу
    for one_process_index in range(0, ACTIVATE_PROCESS_COUNT):
        # Указываем как аргументы очередь задач и общий объект списка для результатов
        process_object = Process(target=worker_process_func, args=(
            tasks_queue, shared_results_list
        ))
        process_list.append(process_object)

    # Делаем перебор нашего списка процессов, после делаем запуск каждого процесса
    for one_process in process_list:
        one_process.start()

    # Делаем перебор списка процессов, после делаем слияние каждого дочернего процесса с главным 
    # процессом, то есть делаем ожидание завершения работы всех процессов
    for one_process in process_list:
        one_process.join()

    end_time = time.time()

    results_list: list = list(shared_results_list)

    print(f"Время всех вычислений: {end_time - started_time} секунд")
    print(results_list)
    print("После сортировки: ")
    print(sorted(results_list))


# Если этот файл был запущен из консоли
if __name__ == "__main__":
    main()

"""
Результат:
Время всех вычислений: 91.7377359867096 секунд
[0, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 
28657, 46368, 75025, 1, 1, 196418, 317811, 121393, 514229, 832040, 1346269, 2178309, 3524578, 
5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
После сортировки:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 
17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 
5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""