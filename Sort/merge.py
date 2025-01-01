def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    right_arr = merge_sort(arr[mid:])
    left_arr = merge_sort(arr[:mid])
    return merge(left_arr, right_arr)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


arr = [78, 56, 45, 76, 89, 90, 567, 45, 12, 3, 4]
sort = merge_sort(arr)
print(sort)

'''
 Big O   -    time - O(n log n),         memory - O(n)
'''