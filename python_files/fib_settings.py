"""
Файл для настройки того, как наши программы для вычислений будут выполняться
"""

import os

# Максимальное число, для которого мы будем считать число Фибоначчи
MAX_FIB_NUMBER = 40

# Число процессов, которые у нас будут исполнять задачи
ACTIVATE_PROCESS_COUNT = (os.cpu_count() * 2) + 1