class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)
        while idx > 0:
            idx -= 1
            if int(num[idx]) % 2:
                return num[:idx + 1]
        return ""
