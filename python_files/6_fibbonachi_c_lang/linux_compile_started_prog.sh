#!/bin/bash

# Файл .sh для компиляции и запуска программ C под Linux

compile_program=0

if [ $compile_program -eq 0 ] ;
    then 
        if gcc 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe;
            then
                compile_program=1
        fi
    fi

if [ $compile_program -eq 0 ];
    then
        if clang 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe;
            then
                compile_program=1
        fi
    fi

if [ $compile_program -eq 0 ]
    then
        if cc 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe;
            then
                compile_program=1
        fi
    fi

if [ $compile_program -eq 1 ];
    then
        echo "Программа скомпилирована! Выполнение..."
        ./6_fibbonachi_exe.exe
        echo "Программа выполнилась"
    elif [ $compile_program -eq 0 ];
        then
            echo "Невозможно найти подходящий компилятор, попробуйте скомпилировать программу сами и запустить"
    fi

compile_program=0