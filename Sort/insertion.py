def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [8, 56, 4, 2, 1, 67, 89, 7]
insertion_sort(arr)
print(arr)

'''
  Big O ->        time - O(n^2),   memory - O(1)
'''
