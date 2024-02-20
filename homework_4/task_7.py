# Перерыв...
# Погружение в Python
# <<7:00->>
# Задание №7
# �Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# �Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# �Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# �При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# �В каждом решении нужно вывести время выполнения
# вычислений.

from random import randint
import asyncio
import time

start = time.time()

arr = [randint(1, 100) for _ in range(10**6)]

summa = 0


async def sum_num_arr(arr):  # функция подсчета суммы элементов массива
    global summa
    for i in arr:
        summa += i


tasks = []

if __name__ == '__main__':

    # разобьем суммирование на 10 потоков порционно подавать массив используя срезы первый цикл счет суммы значений
    # массива от 0 до 100 элемента, второй цикл от 100_001 до 200_000 и так до 1000_000
    for i in range(10):
        start_index = i*100_000
        end_index = start_index + 100_000
        task = asyncio.ensure_future( sum_num_arr(arr[start_index:end_index]))
        tasks.append(task)

    loop = asyncio.get_event_loop()  # получили цикл событий в переменной loop
    loop.run_until_complete(asyncio.wait(tasks))  # запуск цикла событий всех задач

    print('конец завершения  потоков')
    print ('Результат', summa)

    end = time.time()
    print("время выполнения суммы :", end - start)


