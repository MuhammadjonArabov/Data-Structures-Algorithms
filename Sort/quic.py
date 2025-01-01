from random import randrange


def quic_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        n = arr.pop(randrange(len(arr)))
        left = [i for i in arr if i <= n]
        right = [i for i in arr if i > n]
        return quic_sort(left) + [n] + quic_sort(right)

arr = [2, 34, 56, 78, 90, 5, 6, 7, 8, 3]
quic = quic_sort(arr)
print(quic)

'''
Big O      -              time - O(n log n) or  O(n^2),          memory - O(log n)
'''
