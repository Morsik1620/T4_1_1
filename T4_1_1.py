


def linear_search (arr, target_ls):

    for i in range(len(arr)):
        if arr[i] == target_ls:
            print(f'value:{arr[i]} == target: {target_ls}')
            return i
    return -1  # Если элемент не найден

 # Пример использования:
arr = [10, 20, 30, 40, 50]
target_ls = 30
print("Индекс элемента:", linear_search (arr, target_ls))





