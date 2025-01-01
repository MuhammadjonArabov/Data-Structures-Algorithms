def liner_search(arr, target):
    for i in range(len(arr)):
        if i == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
target = 5
result = liner_search(arr, target)
if result != -1:
    print(f"Element {target} indeksda topildi: {result}")
else:
    print(f"Element {target} topilmadi.")

'''
 Big O - >     time - O(n), memory - O(1)
'''