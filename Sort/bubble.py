def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [2, 3, 4, 6, 7, 8, 9]
bubble = bubble_sort(arr)
print(bubble)

'''
  Big O      - >        time - O(n^2),       memory - O(1)
'''



