/*
Файл, который просто содержит функцию для вычисления числа фибоначчи на языке C++
*/

// Делаем создание структуры для больших чисел
typedef long long int int64;

extern "C" int64 fibbonachi_comp(int64 number) {
    if (number == 0) {
        return 0;
    }

    if (number < 2) {
        return 1;
    }

    int64 fib_number = fibbonachi_comp(number - 1) + fibbonachi_comp(number - 2);
    return fib_number;
}

