#!/bin/bash

# Файл .sh для компилирирования и создания Shared object (общих объектов), которые смогут использоваться внутри python файлов

so_create=0

if [ $so_create -eq 0 ];
    then
        # Пробуем создать общий файл программы
        if g++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o linux_object_lib.o;
            then
                # Пробуем создать Shared object (библиотеку) при помощи общего файла программы
                if g++ -shared -Wl,-soname,linux_fib_library.so -o linux_fib_library.so linux_object_lib.o;
                    then
                        so_create=1
                else
                    rm linux_object_lib.o
                fi
        fi

fi

if [ $so_create -eq 0 ];
    then
        # Пробуем создать общий файл программы
        if c++ -shared -c -fPIC 8_fibbonachi_computing.cpp -o linux_object_lib.o;
            then
                # Пробуем создать Shared object (библиотеку) при помощи общего файла программы
                if c++ -shared -Wl,-soname,linux_fib_library.so -o linux_fib_library.so linux_object_lib.o;
                    then 
                        so_create=1
                else
                    rm linux_object_lib.o
                fi
        fi
fi

if [ $so_create -eq 1 ];
    then
        echo Shared object '(файл библиотеки)' был создан
        echo Перемещение получившихся файлов в каталог "library_files"
        mv linux_fib_library.so library_files/
        mv linux_object_lib.o library_files/

else
    echo Не удалось создать Shared object, попробуйте это сделать при помощи своего компилятора
fi