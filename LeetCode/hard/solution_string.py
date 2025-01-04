'''
3. Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length, start = 0, 0
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length


solution3 = Solution3()
print(solution3.lengthOfLongestSubstring("abacabc"))
