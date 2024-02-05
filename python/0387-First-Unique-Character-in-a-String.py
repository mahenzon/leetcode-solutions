# `collections` is already imported in LeetCode
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counts = collections.defaultdict(int)
        # for c in s:
        #     counts[c] += 1
        counts = collections.Counter(s)
        for idx, c in enumerate(s):
            if counts[c] == 1:
                return idx
        return -1
