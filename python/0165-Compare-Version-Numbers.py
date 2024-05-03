# `itertools` is already imported in LeetCode
import itertools


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")

        for part1, part2 in itertools.zip_longest(parts1, parts2, fillvalue=0):
            p1 = int(part1)
            p2 = int(part2)

            if p1 > p2:
                return 1
            if p1 < p2:
                return -1

        return 0
