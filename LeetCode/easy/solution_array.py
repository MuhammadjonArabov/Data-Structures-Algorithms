from itertools import count
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

# ----------------------------------------------------------------------------------------------------------------------
''' Time : O(n**2),    Memory: O(n**2) '''


def generate(numRows):
    arr = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = arr[i - 1][j - 1] + arr[i - 1][j]
        arr.append(row)
    return arr[-1]


print(generate(5))


# ----------------------------------------------------------------------------------------------------------------------

def getRow(rowIndex):
    row = [1] * (rowIndex + 1)

    for i in range(1, rowIndex):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]
    return row

print(3)

# ----------------------------------------------------------------------------------------------------------------------

def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

print(maxProfit([5, 2, 1, 6, 7, 9]))

# ----------------------------------------------------------------------------------------------------------------------

def f(son):
    r = 0
    for i in son:
        r ^= i
    return r

print(f([2,2,1]))

#-----------------------------------------------------------------------------------------------------------------------

def majorityElement(nums):
    majority = {}
    for i in nums:
        if i in majority:
            majority[i] += 1
        else:
            majority[i] = 1
        return max(majority, key=majority.get)

print(majorityElement([3,2,3]))

#-----------------------------------------------------------------------------------------------------------------------


def containsNearbyDuplicate(nums, k):
    indexes = {}
    for i, num in enumerate(nums):
        if num in indexes and abs(i - indexes[num]) <= k:
            return True
        indexes[num] = i
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))






