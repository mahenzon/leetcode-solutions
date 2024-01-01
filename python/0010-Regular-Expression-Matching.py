class Solution:
    def dfs(self, i, j) -> bool:
        key = (i, j)
        if key in self.cache:
            return self.cache[key]

        if i >= len(self.s) and j >= len(self.p):
            return True

        if j >= len(self.p):
            return False

        # i in bounds
        match = i < len(self.s) and (
            # exact match
            self.s[i] == self.p[j]
            # or matches any single character
            or self.p[j] == "."
        )
        next_j = j + 1
        p_star = next_j < len(self.p) and self.p[next_j] == "*"
        if p_star:
            res = (
                # use star: current matches and next in s matches
                match and self.dfs(i + 1, j)
                # don't use star: skip current and star char
                or self.dfs(i, j + 2)
            )
            self.cache[key] = res
            return res

        if match:
            # current ok, check next
            res = self.dfs(i + 1, j + 1)
            self.cache[key] = res
            return res

        self.cache[key] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.cache = {}
        return self.dfs(0, 0)
