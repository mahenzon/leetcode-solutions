# `Counter` from `collections` is already imported in LeetCode
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # prioritize CPU:
        # counts1 = Counter(nums1)
        # counts2 = Counter(nums2)
        # res = []
        # for n, c1 in counts1.items():
        #     if c2 := counts2.get(n):
        #         for _ in range(min(c1, c2)):
        #             res.append(n)
        #
        # return res

        # prioritize RAM:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counts1 = Counter(nums1)
        res = []
        for n in nums2:
            if c := counts1.get(n):
                res.append(n)
                counts1[n] -= 1

        return res
