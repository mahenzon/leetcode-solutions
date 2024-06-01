class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(
            abs(ord(s[idx]) - ord(s[idx - 1]))
            for idx in range(1, len(s))
        )
