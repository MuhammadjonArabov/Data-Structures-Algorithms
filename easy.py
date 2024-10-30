'''1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''

class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
print(solution.twoSum([1, 2, 3, 4, 5, 6], 9))
print(solution.twoSum([11, 2, 3, 41, 52, 63], 5))
print(solution.twoSum([13, 25, 39, 40, 55, 6], 19))

#======================================================================================================================

'''2. Given an integer x, return true if x is a palindrome and false otherwise.'''
