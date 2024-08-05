# `Counter` is already imported in LeetCode
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        for el in arr:
            if counts[el] == 1:
                k -= 1
                if not k:
                    return el

        return ""
