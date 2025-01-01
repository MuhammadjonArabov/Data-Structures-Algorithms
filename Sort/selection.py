def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [4, 44, 34, 56, 78, 98, 0]
selection = selection_sort(arr)
print(selection)

'''
Big O   -    time - O(n^2),   memory - O(1)
'''
