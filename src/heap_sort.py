arr = [1, 15, 14, 13, 11, 10, 12, 5, 9, 2, 6, 3, 8, 7, 4]

def heapify(data, start, end):
    root = start

    while True:
        # Вычисляем индекс левого потомка
        child = root * 2 + 1

        # Если вышли за границы массива - завершаем
        if child > end:
            break

        # Выбираем наибольший из потомков
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        # Если потомок больше корня - меняем их местами
        if data[root] < data[child]:
            # Обмен значений
            data[root], data[child] = data[child], data[root]
            # Сдвигаем корень вниз
            root = child
        else:
            # Если не нужно менять - выходим из цикла
            break

def heap_sort(arr):
    n = len(arr)

    # Строим кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n - 1)

    # Извлекаем элементы по одному
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i - 1)

    return arr

print(heap_sort(arr))





