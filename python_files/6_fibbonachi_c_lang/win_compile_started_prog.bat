:: bat файл для компиляции и запуска программы на C++ под Windows

:: Убираем лишний вывод в терминал
@echo off

:: Ставим кодовую страницу терминала на UTF-8
chcp 65001

set compile_program=0

if %compile_program% EQU 0 (
    gcc 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 0 (
    mingw32-gcc.exe 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 0 (
    clang 6_fibbonachi_c.c -o 6_fibbonachi_exe.exe && set compile_program=1
)

if %compile_program% EQU 1 (
    echo Программа скомпилирована! Выполнение...
    6_fibbonachi_exe.exe
    echo Выполнение завершено
) else (
    echo Невозможно найти подходящий компилятор, попробуйте скомпилировать программу сами и запустить
)

set compile_program=0

pause