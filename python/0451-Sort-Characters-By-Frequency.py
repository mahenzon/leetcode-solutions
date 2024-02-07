# `collections` is already imported in LeetCode
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        buckets = collections.defaultdict(list)
        for char, count in counts.items():
            buckets[count].append(char)

        parts = []
        for count in range(len(s), 0, -1):
            if count not in buckets:
                continue
            for char in buckets[count]:
                parts.append(char * count)
        return "".join(parts)
