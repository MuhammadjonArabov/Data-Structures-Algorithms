def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        print(left_arr[i], right_arr[j])
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    # result.extend(left_arr[i:])
    # result.extend(right_arr[j:])

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1

    return result


arr = [4, 2, 3, 1]
sort = merge_sort(arr)
print(sort)

'''
 Big O   -    time - O(n log n),         memory - O(n)
'''
