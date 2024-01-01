class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        pos = {}
        for idx, c in enumerate(s):
            if c in pos:
                res = max(res, idx - pos[c] - 1)
            else:
                pos[c] = idx

        return res
