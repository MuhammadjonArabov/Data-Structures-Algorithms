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