class Solution:
    max_val = 10**6 + 1
    min_val = -max_val

    def get_middle_vals(self, idx: int, nums: List[int]) -> Tuple[int, int]:
        max_left = nums[idx] if idx >= 0 else self.min_val
        next_idx = idx + 1
        min_right = nums[next_idx] if next_idx < len(nums) else self.max_val
        return max_left, min_right

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = len(nums1)
        s2 = len(nums2)
        if s1 > s2:
            return self.findMedianSortedArrays(nums2, nums1)

        total = s1 + s2
        half, is_odd = divmod(total, 2)

        left = 0
        right = s1 - 1

        while True:
            idx1 = left + (right - left) // 2
            idx2 = half - idx1 - 2

            max_left_1, min_right_1 = self.get_middle_vals(idx1, nums1)
            max_left_2, min_right_2 = self.get_middle_vals(idx2, nums2)

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if is_odd:
                    return min(min_right_1, min_right_2)
                return (
                    min(min_right_1, min_right_2)
                    +
                    max(max_left_1, max_left_2)
                ) / 2

            if max_left_1 > min_right_2:
                right = idx1 - 1
            else:
                left = idx1 + 1
