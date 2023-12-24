class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        last = ""
        for i, c in enumerate(s):
            if i % 2:
                count += c == "0"
            else:
                count += c == "1"

        return min(count, len(s) - count)
