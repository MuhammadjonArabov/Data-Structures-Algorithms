from pandas.io.formats.format import return_docstring


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


# -----------------------------------------------------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------------------------------------------------

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1




sol = Solution()
print(sol.validMountainArray([2, 1]))
print(sol.validMountainArray([3, 5, 5]))
print(sol.validMountainArray([0, 3, 2, 1]))



