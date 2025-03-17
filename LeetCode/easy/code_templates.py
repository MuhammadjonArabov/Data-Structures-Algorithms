def duplicateZeros(arr):
    n = len(arr)
    i = 0
    while i < n:
       if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
       i += 1
    return arr

print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))

#-----------------------------------------------------------------------------------------------------------------------

def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)