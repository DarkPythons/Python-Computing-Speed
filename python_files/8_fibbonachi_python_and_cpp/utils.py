import sys

def add_relative_import():
    sys.path.append("../")

class CppLibraryNotExistsError(Exception):
    pass

error_cpp_not_found = CppLibraryNotExistsError("""
\n
Динамическая библиотека (DLL) или Shared object (общий объект) не найден.
Воспользуйтесь windows_create_dll.bat для создания DLL если вы под Windows,
Или linux_create_shr_obj.sh для создания Shared object если вы под Linux.
""")