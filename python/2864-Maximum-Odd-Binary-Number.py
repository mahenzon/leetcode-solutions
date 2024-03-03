class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        left = 0
        for idx, val in enumerate(s):
            if val == "1":
                s[left], s[idx] = s[idx], s[left]
                left += 1
        s[left - 1], s[-1] = s[-1], s[left - 1]
        return "".join(s)
