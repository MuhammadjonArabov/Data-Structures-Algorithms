'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

class Solution10(object):
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                return first_match and match(i + 1, j + 1)

        return match(0, 0)


solution10 = Solution10()
print(solution10.isMatch("aa", "a*"))  # True
print(solution10.isMatch("mississippi", "mis*is*p*."))  # False
print(solution10.isMatch("ab", ".*"))  # True

# =======================================================================================================================

'''4. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).'''

from typing import List


class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = nums1 + nums2
        m.sort()
        n = len(m)

        if n % 2 == 1:
            return m[n // 2]
        else:
            return (m[n // 2] + m[n // 2 - 1]) / 2


solution4 = Solution4()
print(solution4.findMedianSortedArrays([22, 23, 24], [25, 26, 27, 28, 29]))
print(solution4.findMedianSortedArrays([22, 23, 24], [25, 26, 27, 28]))

#=======================================================================================================================

'''You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original 
string where spaces will be added. Each space should be inserted before the character at the given index.'''

class Solution2119:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = []
        prev = 0
        for i in spaces:
            l.append(s[prev:i])
            prev = i
        l.append(s[prev:])
        return ' '.join(l)

solution2119 = Solution2119()
print(solution2119.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
print(solution2119.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))


