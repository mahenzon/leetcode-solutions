class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [len(s)] * len(s)
        closest_idx = len(s) - 1
        for idx, char in enumerate(s):
            if char == c:
                closest_idx = idx
            res[idx] = abs(idx - closest_idx)

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == c:
                closest_idx = idx
            res[idx] = min(
                res[idx],
                abs(idx - closest_idx),
            )

        return res
