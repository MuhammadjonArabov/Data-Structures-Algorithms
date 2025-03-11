from typing import Iterable


def merge_two_arrays(arr1: list[int], arr2: list[int]) -> Iterable[int]:
    i = j = 0
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            yield arr1[i]
            i += 1
        else:
            yield arr2[j]
            j += 1

    while i < n:
        yield arr1[i]
        i += 1

    while j < m:
        yield arr2[j]
        j += 1


print(list(merge_two_arrays([1, 2, 3, 4, 5], [2, 3, 6, 7, 8, 9])))

# -----------------------------------------------------------------------------------------------------------------------


def generate(numRows):
    arr = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = arr[i - 1][j - 1] + arr[i - 1][j]
        arr.append(row)
    return arr


print(generate(5))
