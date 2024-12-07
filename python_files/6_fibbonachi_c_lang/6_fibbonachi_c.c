/*
Код шестого способа вычисления чисел Фибоначчи.
Использование другого языка программирования, сам по себе python является медленным языком из-за его высокоуровневости и интерпретируемости, что если переписать тот же алгоритм на низкоуровневом языке и комплириуемом
*/

#include <stdio.h>
#include <time.h>

// Структура данных для больших чисел
typedef long long int int64;

// Прототип функции для нахождения чисел фибоначчи
int64 fibbonachi(int64 number);

int main(void) {
    // Максимальное число, для которого нужно будет вычислить число фибоначчи
    int MAX_FIB_NUMBER = 40;

    int64 tasks_array[MAX_FIB_NUMBER+1];
    int64 results_array[MAX_FIB_NUMBER+1];

    // Цикл для заполнения массива задач нашими числами
    for (int64 one_number_task = 0; one_number_task < MAX_FIB_NUMBER+1; one_number_task++) {
        int index = (int)one_number_task;
        tasks_array[index] = one_number_task;
    }

    clock_t start_time = clock();

    // Цикл, где из нашего массива задач будет браться число, после чего помещаться в функцию для нахождения чисел фибоначчи, после чего помещаться в массив результатов
    for (int index = 0; index < MAX_FIB_NUMBER+1; index++) {
        int64 number = tasks_array[index];
        int64 fib_number = fibbonachi(number);
        results_array[index] = fib_number;
    }

    clock_t end_time = clock();

    clock_t full_time = end_time - start_time;

    printf("Время всех вычислений: %lf секунд\n", (double)full_time/CLOCKS_PER_SEC);

    // Цикл вывода чисел фибоначчи из массива результатов
    for (int index = 0; index < MAX_FIB_NUMBER+1; index++) {
        printf("%lli ", results_array[index]);
    }

    printf("\n");

    return 0;
}


int64 fibbonachi(int64 number) {
    // Функция для вычисления чисел фибоначчи

    if (number == 0) {
        return 0;
    }

    if (number < 2) {
        return 1;
    }

    int64 fib_number = fibbonachi(number - 2) + fibbonachi(number - 1);
    return fib_number;
}

/*
Результат:
Время всех вычислений: 6.203000 секунд
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155
*/