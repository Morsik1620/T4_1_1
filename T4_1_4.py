
#Сравните время выполнения линейного поиска для разных
#размеров списков (например, 10, 100, 1000 элементов). Постройте
#график зависимости времени выполнения от размера списка

import timeit

def make_arr (arr1):
    for i in range(0, arr1):
        arr3.append(i) # Добавляю значение в список
    arr3.sort(reverse=True)
    return arr3

t = '''def list_t(arr3, target_t):
            for i in range(len(arr3)):
                if arr3[i] == target_t:
                    print (f'Индекс элемента:{i}    Значение элемента:{random_list[i]}')
                    return i'''

arr2=[10, 100, 1000]

for arr1 in arr2:
    arr3=[]
    target_t = 0
    print (f'Рассмотрим список из: {arr1} символов')
    print(f'Найдем значение {target_t}')
    make_arr(arr1)
    print("Список чисел:", arr3)  # Вывод списка для отладки
    time = timeit.timeit(stmt=t, number=100000)
    print(f'Потраченное время на выполнение кода: {time:.6f} секунд')  # number=100 сколько раз будет выполняться код
