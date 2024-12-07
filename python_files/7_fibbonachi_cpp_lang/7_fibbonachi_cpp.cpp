/*
Код седьмого способа вычисления чисел фибоначчи.
Использование c++ для нахождения чисел фибоначчи, при помощи рекурсивной функции
*/

using namespace std;

#include <vector>
#include <iostream>
#include <stdio.h>
#include <time.h>

// Структура для больших чисел
typedef long long int int64;

int64 fibbonachi(int64 number);

int main(void) {
    // Максимальное число, для которого нужно будет искать число фибоначчи
    int MAX_FIB_NUMBER = 40;

    vector<int64> tasks_list;
    vector<int64> results_list;

    // Делаем перебор от 0 до максимального числа для которого нужно найти число фибоначчи, помещая все числа в вектор задач
    for (int64 one_number_task = 0; one_number_task < MAX_FIB_NUMBER+1; one_number_task++) {
        tasks_list.push_back(one_number_task);
    }

    clock_t start_time = clock();

    // Делаем получение задачи (числа) по индексу, после чего помещаем его в фукцию для вычисления числа фибоначчи, помещая результат в вектор результатов
    for (int index = 0; index < MAX_FIB_NUMBER+1; index++) {
        int64 number = tasks_list[index];
        int64 fib_number = fibbonachi(number);
        results_list.push_back(fib_number);
    }

    clock_t end_time = clock();

    clock_t full_time = end_time - start_time;

    printf("Все вычисления заняли: %lf секунд\n", (double)full_time/CLOCKS_PER_SEC);


    for (auto fib_number : results_list) {
        cout << fib_number << " ";
    }

    cout << endl;

    printf("\n");

}

int64 fibbonachi(int64 number) {
    if (number == 0) {
        return 0;
    }

    if (number < 2) {
        return 1;
    }

    int64 fib_number = fibbonachi(number - 1) + fibbonachi(number - 2);
    return fib_number;
}

/*
Результат:
Все вычисления заняли: 5.367000 секунд
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155
*/