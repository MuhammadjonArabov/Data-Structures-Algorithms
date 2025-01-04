'''
13. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.  # Time O(n). # Memory O(1)
'''
from typing import List

from pandas.io.formats.format import return_docstring


class Solution13:
    def romanToInto(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in s:
            current_value = roman_map[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        return total


solution13 = Solution13()
print(solution13.romanToInto('IV'))
print(solution13.romanToInto('VII'))

'''
14. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".   # time - O(n*m),  memory - O(1)
'''


class Solution14:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


solution14 = Solution14()
print(solution14.longestCommonPrefix(["flower", "flow", "flight"]))

'''
20. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. time - O(n), memory - O(n)
'''


class Solution20:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack


solution20 = Solution20()
print(solution20.isValid("()"))
print(solution20.isValid("()[]{"))

'''
28. Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.  time - O(n + m)      memory - O(1)
'''


class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        if index != -1 and haystack[index: index + len(needle)] == needle:
            return index
        else:
            return -1


solution28 = Solution28()
print(solution28.strStr("sadbutsad", "sad"))
print(solution28.strStr("sadbutsad", "sadi"))

'''58. Given a string s consisting of words and spaces, return the length of the last word in the string. time - O(n), memory - O(n)'''


class Solution58:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


solution58 = Solution58()
print(solution58.lengthOfLastWord(" fly me   to   the moon "))

'''
125. A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''

class Solution125:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filter_s = ''.join(char for char in s if char.isalnum())
        return filter_s == filter_s[::-1]

'''
205. Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''
solution125 = Solution125()
print(solution125.isPalindrome("amma"))

class Solution205:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_s, mapping_t = {}, {}
        for char_s, char_t in zip(s, t):
            if char_s in mapping_s:
                if mapping_s[char_s] != char_t:
                    return False
            else:
                mapping_s[char_s] = char_t

            if char_t in mapping_t:
                if mapping_t[char_t] != char_s:
                    return False
            else:
                mapping_t[char_t] = char_s
        return True


solution205 = Solution205()
print(solution205.isIsomorphic('add', 'off'))
print(solution205.isIsomorphic('hello', 'off'))