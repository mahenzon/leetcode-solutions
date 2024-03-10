class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(nums2)
        known = set(nums1)
        result = []
        for num in nums2:
            if num in known:
                result.append(num)
                known.remove(num)
        return result
