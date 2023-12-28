class Solution:
    def count(self, i, remaining, prev_char, prev_count) -> int:
        key = (i, remaining, prev_char, prev_count)
        if key in self.cache:
            return self.cache[key]
        if remaining < 0:
            # return max available
            return 101
        if i == len(self.s):
            return 0

        if self.s[i] == prev_char:
            # increase by one if groun by an order of magnitude
            incr = prev_count in (1, 9, 99)
            res = incr + self.count(i + 1, remaining, prev_char, prev_count + 1)
        else:
            res = min(
                # delete this char
                self.count(i + 1, remaining - 1, prev_char, prev_count),
                # don't delete this char
                1 + self.count(i + 1, remaining, self.s[i], 1),
            )

        self.cache[key] = res
        return res

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.cache = {}
        self.s = s
        return self.count(0, k, "", 0)
