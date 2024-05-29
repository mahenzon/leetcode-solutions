class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        for idx in range(len(s) - 1, 0, -1):
            num = (int(s[idx]) + carry) % 2
            res += 1
            if num:
                carry = 1
                res += 1
        return res + carry
