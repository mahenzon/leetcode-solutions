class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx_s = 0
        idx_t = 0
        res = 0
        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
                idx_t += 1
            else:
                idx_s += 1

        return len(t) - idx_t
