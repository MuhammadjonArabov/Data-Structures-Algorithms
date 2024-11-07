'''1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''


class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
print(solution.twoSum([1, 2, 3, 4, 5, 6], 9))
print(solution.twoSum([11, 2, 3, 41, 52, 63], 5))
print(solution.twoSum([13, 25, 39, 40, 55, 6], 19))

# ======================================================================================================================

'''9. Given an integer x, return true if x is a palindrome and false otherwise.'''


class Solution9():
    def isPalindrome(self, x):
        if x < 0:
            return False
        str_x = str(x)
        return str_x == str_x[::-1]


solution9 = Solution9()
print(solution9.isPalindrome(121))
print(solution9.isPalindrome(12))
print(solution9.isPalindrome(1221))

# ======================================================================================================================

'''
13 Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''


class Solution13():
    def romanToInt(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


solution13 = Solution13()
print(solution13.romanToInt('IV'))

# =======================================================================================================================

'''14. Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''


class Solution14():
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


solution14 = Solution14()
print(solution14.longestCommonPrefix(['olma', 'olcha', 'olxora']))
print(solution14.longestCommonPrefix(['olma', 'olcha', 'shaftoli']))

# =======================================================================================================================

'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''


class Solution20():
    def isValid(self, s):
        char_oll = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in char_oll:
                top_char = stack.pop() if stack else None
                if char_oll[i] != top_char:
                    return False
            else:
                stack.append(i)
        return not stack

solution20 = Solution20()
print(solution20.isValid('()[]'))
print(solution20.isValid('()]'))