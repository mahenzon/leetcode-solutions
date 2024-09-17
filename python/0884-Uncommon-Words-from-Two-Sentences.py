# `collections` is already imported in LeetCode
import collections


class Solution:

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = collections.Counter(s1.split())
        counts.update(s2.split())
        return [word for word, count in counts.items() if count == 1]
