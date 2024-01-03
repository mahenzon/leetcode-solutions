class Solution:
    def dfs(self, idx_s, idx_p):
        key = (idx_s, idx_p)
        if key in self.cache:
            return self.cache[key]

        if idx_s >= len(self.s) and idx_p >= len(self.p):
            # cache? no need
            return True

        if idx_p >= len(self.p):
            # s not fully checked, but p is exausted
            return False

        p_star = self.p[idx_p] == "*"

        # so, idx_s is exausted
        # match if idx_s is in bounds and char matches
        match = idx_s < len(self.s) and (
            # exact match
            self.s[idx_s] == self.p[idx_p]
            # or matches any single char
            or self.p[idx_p] == "?"
            # or star match
            or p_star
        )

        if p_star:
            res = (
                # use star (current char len 1+):
                # current char matches and next one matches too
                match and self.dfs(idx_s + 1, idx_p)
                # skip star char (current char len 0)
                or self.dfs(idx_s, idx_p + 1)
            )
            self.cache[key] = res
            return res

        if match:
            # current char ok, check next
            res = self.dfs(idx_s + 1, idx_p + 1)
            self.cache[key] = res
            return res

        self.cache[key] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.cache = {}

        return self.dfs(0, 0)
