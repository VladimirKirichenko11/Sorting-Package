# Вспомогательная функция для быстрой сортировки
def _partition(arr, low, high, reverse=False):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if (not reverse and arr[j] <= pivot) or (reverse and arr[j] >= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_recursive(arr, low, high, reverse=False):
    if low < high:
        pi = _partition(arr, low, high, reverse)
        _quick_sort_recursive(arr, low, pi - 1, reverse)
        _quick_sort_recursive(arr, pi + 1, high, reverse)


def quick_sort(arr, reverse=False):
    if not arr:
        return arr

    arr = arr.copy()
    _quick_sort_recursive(arr, 0, len(arr) - 1, reverse)
    return arr
