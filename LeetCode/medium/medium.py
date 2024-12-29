from builtins import str


class Solution8(object):
    def myAtoi(self, s: str):
        s = s.lstrip()
        if not s:
            return 0

        n = 1
        if s[0] == '-':
            n = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        result *= n

        if result > 2**31 - 1:
            return result
        if result < -2**31:
            return result
        return result

solution8 = Solution8()
print(solution8.myAtoi('   -042'))

#=======================================================================================================================

'''You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special,
 whereas the strings "ddd", "zz", and "f" are special.'''

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_length = -1

        for length in range(1, n + 1):
            freq = {}
            for i in range(n - length + 1):
                substring = s[i:i + length]
                if len(set(substring)) == 1:
                    freq[substring] = freq.get(substring, 0) + 1


            for substring, count in freq.items():
                if count >= 3:
                    max_length = max(max_length, len(substring))

        return max_length


str = 'salom'
print(str.encode('utf-8'))
