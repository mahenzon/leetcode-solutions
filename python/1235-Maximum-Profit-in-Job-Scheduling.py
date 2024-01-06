class Solution:
    def dfs(self, i):
        if i >= len(self.intervals):
            return 0
        if i in self.cache:
            return self.cache[i]

        start, end, profit = self.intervals[i]
        # skip this one, use next
        res = self.dfs(i + 1)

        # include this one
        # end should be higher that start
        pos = bisect.bisect(self.intervals, (end, -1, -1))

        # choose this one or next
        res = max(res, profit + self.dfs(pos))
        self.cache[i] = res
        return res

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.intervals = sorted(zip(startTime, endTime, profit))
        self.cache = {}
        return self.dfs(0)
