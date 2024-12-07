:: bat файл для создания DLL то есть динамической библиотеки, которая будет встраивать свой код в момент исполнения программы

:: Отключаем лишний вывод
@echo off

:: Изменяем кодовую страницу на UTF-8
chcp 65001

set dll_create=0


if %dll_create% EQU 0 (
    :: Создание объекта программы
    :: Из объекта программы делаем создание DLL
    g++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o windows_library_object.o && g++ -shared -Wl,-soname,windows_library_fib.dll -o windows_library_fib.dll windows_library_object.o && set dll_create=1
)

if %dll_create% EQU 0 (
    :: Создание объекта программы
    :: Из объекта программы делаем создание DLL
    c++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o windows_library_object.o && c++ -shared -Wl,-soname,windows_library_fib.dll -o windows_library_fib.dll windows_library_object.o && set dll_create=1
)

if %dll_create% EQU 0 (
    :: Создание объекта программы
    :: Из объекта программы делаем создание DLL
    mingw32-c++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o windows_library_object.o && mingw32-c++ -shared -Wl,-soname,windows_library_fib.dll -o windows_library_fib.dll windows_library_object.o && set dll_create=1
)

if %dll_create% EQU 0 (
    :: Создание объекта программы
    :: Из объекта программы делаем создание DLL
    mingw32-g++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o windows_library_object.o && mingw32-g++ -shared -Wl,-soname,windows_library_fib.dll -o windows_library_fib.dll windows_library_object.o && set dll_create=1
)


:: Если динамическая библиотека была создана
if %dll_create% EQU 1 (
    echo Динамическая библиотека была успешно создана
    echo Перемещение файлов библиотеки в директорию "library_files"
    move windows_library_object.o library_files && echo Новый файл windows_library_object.o был перемещен
    move windows_library_fib.dll library_files && echo Новый файл windows_library_fib.dll был перемещен

) else (
    echo Программе не удалось создать динамическую библиотеку
)

pause