class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            current = s[left]
            while left <= right and s[left] == current:
                left += 1
            while right >= left and s[right] == current:
                right -= 1

        return right - left + 1
