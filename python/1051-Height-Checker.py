# `itertools` is already imported in LeetCode
import itertools


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # bucket (count) sort
        counts = [0] * 101
        for h in heights:
            counts[h] += 1

        expected = [
            (height,) * count
            for height, count
            in enumerate(counts)
            if count
        ]
        return sum(
            h != e
            for h, e in zip(
                heights,
                itertools.chain.from_iterable(expected),
            )
        )
