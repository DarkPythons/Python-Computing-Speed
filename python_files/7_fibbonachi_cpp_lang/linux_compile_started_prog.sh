#!/bin/bash

# Файл .sh для компилирования и запуска программ под Linux

compile_program=0

if [ $compile_program -eq 0 ];
    then
        if g++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe;
            then 
                compile_program=1
        fi
    fi

if [ $compile_program -eq 0 ];
    then
        if c++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe;
            then
                compile_program=1
        fi
    fi

if [ $compile_program -eq 1 ];
    then 
        echo "Программа скомпилирована! Выполнение..."
        ./7_fibbonachi_exe.exe
        echo "Выполнение завершено"        

    elif [ $compile_program -eq 0 ];
        then 
            echo "Невозможно найти подходящий компилятор, попробуйте скомпилировать программу сами и запустить"
    fi

compile_program=0