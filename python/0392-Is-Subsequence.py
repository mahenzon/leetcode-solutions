class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s = 0
        idx_t = 0
        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
            idx_t += 1

        return idx_s == len(s)
