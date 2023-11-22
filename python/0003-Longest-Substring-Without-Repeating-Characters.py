class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        known_chars = set()
        for right, right_char in enumerate(s):
            while right_char in known_chars:
                known_chars.remove(s[left])
                left += 1
            known_chars.add(right_char)
            result = max(result, right - left + 1)
        return result
