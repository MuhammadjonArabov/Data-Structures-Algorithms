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
