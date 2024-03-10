class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        known = set(nums1)
        result = []
        for num in nums2:
            if num in known:
                result.append(num)
                known.remove(num)
        return result
