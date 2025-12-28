# Функция для слияния двух отсортированных массивов
def _merge(left, right, reverse=False):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (not reverse and left[i] <= right[j]) or (reverse and left[i] >= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr.copy() if arr else arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], reverse)
    right = merge_sort(arr[mid:], reverse)

    return _merge(left, right, reverse)
