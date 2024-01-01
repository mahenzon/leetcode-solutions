class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_i = 0
        s_i = 0
        while g_i < len(g) and s_i < len(s):
            if g[g_i] <= s[s_i]:
                g_i += 1
            s_i += 1
        return g_i
