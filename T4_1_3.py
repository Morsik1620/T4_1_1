import random

def random_list_f(random_list, target_rl):
    for i in range(len(random_list)):
        if random_list[i]==target_rl:
            print (f'Индекс элемента:{i}    Значение элемента:{random_list[i]}')
            return i
    return -1

random_list = [random.randint(0, 99) for _ in range(100)] # создаю список случайных чисел
print("Список случайных чисел:", random_list)  #Вывод списка для отладки
target_rl = 50
print (random_list_f(random_list, target_rl))

