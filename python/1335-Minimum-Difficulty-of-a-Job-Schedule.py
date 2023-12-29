class Solution:
    def dfs(self, idx, days, cur_max):
        if idx == self.jd_len:
            return 0 if days == 0 else 10 ** 5
        if days == 0:
            return 10 ** 5

        key = (idx, days, cur_max)
        if key in self.cache:
            return self.cache[key]

        cur_max = max(cur_max, self.jd[idx])
        res = min(
            # continue same day
            self.dfs(1 + idx, days, cur_max),
            # end this day, start next
            cur_max + self.dfs(1 + idx, days - 1, -1)
        )
        self.cache[key] = res
        return res

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.cache = {}
        self.jd = jobDifficulty
        self.jd_len = len(self.jd)
        if len(jobDifficulty) < d:
            return -1

        return self.dfs(0, d, -1)
