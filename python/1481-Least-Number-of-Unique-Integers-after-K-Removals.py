# `collections` is already imported in LeetCode
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.Counter(arr)
        bucket = [0] * (len(arr) + 1)
        for count in counts.values():
            bucket[count] += 1

        # counts keys only
        result = len(counts)

        for count, frequency in enumerate(bucket):
            if not (count and frequency):
                continue
            if k >= (to_remove := count * frequency):
                k -= to_remove
                result -= frequency
            else:
                to_remove = k // count
                result -= to_remove
                break
        return result
