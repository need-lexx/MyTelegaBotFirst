#-----------------ЗАДАЧА №8-----------------------#


'''Рассмотрим задачу, связанную с выполнением ряда действий
над функцией, использующей декораторы. Необходимо создать
несколько декораторов, которые выполняют следующие
действия:

1. Замер времени выполнения функции: декоратор должен
замерять и выводить время, затраченное на выполнение
функции.

2. Кэширование результатов: декоратор должен кэшировать
результаты вызова функции для предотвращения
повторных вычислений при одинаковых входных данных
(txt документ или можно использовать БД).

3. Логирование вызовов: декоратор должен логировать
вызовы функции, включая параметры и возвращаемое
значение (не обязательно).'''
import time

def dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функция {func.__name__!r} выполнена за {elapsed_time:.4f} секунд.")
        return result     
    return wrapper


def cache(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    data = file.read().split('\n')
                    index = data.index(key)
                    result = data[index + 1]
                    print(f"Результат функции {func.__name__!r} найден в кэше.")
                    return result
            except ValueError:
                result = func(*args, **kwargs)
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f"{key}\n")
                    file.write(f"{result}\n")
                return result
        return wrapper
    return decorator

@dec 
@cache('Task_8/Запись результатов из 8-ой задачи.txt')   
def test (a: int, b: int):
    time.sleep(2)
    return a * b
    
test(2, 3)
test(2, 3)    

