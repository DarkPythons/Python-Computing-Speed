:: bat файл для компиляции и запуска программы на C++ под Windows

:: Отключаем лишние выводы терминала
@echo off

:: Изменяем кодовую страницу на UTF-8
chcp 65001

set compile_program=0

if %compile_program% EQU 0 (
    c++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 0 (
    g++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 0 (
    mingw32-c++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 0 (
    mingw32-g++ 7_fibbonachi_cpp.cpp -o 7_fibbonachi_exe.exe && set compile_program=1
)


if %compile_program% EQU 1 (
    echo Программа скомпилирована! выполнение...
    7_fibbonachi_exe.exe
    echo Выполнение завершено
) else (
    echo Невозможно найти подходящий компилятор, попробуйте скомпилировать программу сами и запустить
)

set compile_program=0

pause