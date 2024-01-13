# `collections` is already imported in LeetCode
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = collections.Counter(s)
        count_t = collections.Counter(t)
        count.subtract(count_t)
        return sum(abs(c) for c in count.values()) // 2
