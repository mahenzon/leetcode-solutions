class Solution:
    after_two = set("0123456")

    def dfs(self, idx) -> int:
        if idx in self.cache:
            return self.cache[idx]
        if self.s[idx] == "0":
            return 0

        res = self.dfs(idx + 1)
        if (
            idx + 1 < len(self.s) and (
                self.s[idx] == "1" or
                (
                    self.s[idx] == "2"
                    and self.s[idx + 1] in self.after_two
                )
            )
        ):
            res += self.dfs(idx + 2)

        self.cache[idx] = res
        return res

    def numDecodings(self, s: str) -> int:
        self.s = s
        self.cache = {len(s): 1}
        return self.dfs(0)
