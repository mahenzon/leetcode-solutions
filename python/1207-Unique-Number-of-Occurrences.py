# `collections` is already imported in LeetCode
import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        seen = set()
        for cnt in count.values():
            if cnt in seen:
                return False
            seen.add(cnt)
        return True
