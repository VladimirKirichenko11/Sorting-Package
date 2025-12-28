# Вспомогательная функция для построения кучи
def _heapify(arr, n, i, reverse=False):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        if not reverse and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        elif reverse and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left

    if right < n:
        if not reverse and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
        elif reverse and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        _heapify(arr, n, largest_or_smallest, reverse)


def heap_sort(arr, reverse=False):
    if not arr:
        return arr

    arr = arr.copy()
    n = len(arr)

    # Построение max-heap (или min-heap для обратной сортировки)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i, reverse)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0, reverse)

    return arr
