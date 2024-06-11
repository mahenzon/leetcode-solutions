# `defaultdict` is already imported in LeetCode
from collections import defaultdict
# `itertools` is already imported in LeetCode
import itertools


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        present_counts = defaultdict(int)
        others = []
        known = set(arr2)
        for num in arr1:
            if num in known:
                present_counts[num] += 1
            else:
                others.append(num)

        present = list(
            itertools.chain.from_iterable(
                (num, ) * present_counts[num]
                for num in arr2
            )
        )
        others.sort()

        return present + others
