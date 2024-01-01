class Solution:
    max_val = 10 ** 6 + 1
    min_val = -max_val

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = len(nums1)
        s2 = len(nums2)
        if s1 > s2:
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = s1 - 1
        total = s1 + s2
        half = total // 2

        while True:
            # idx for nums1
            idx1 = left + (right - left) // 2
            # idx for nums2
            idx2 = half - idx1 - 2

            max_left_1 = nums1[idx1] if idx1 >= 0 else self.min_val
            min_right_1 = nums1[idx1 + 1] if (idx1 + 1) < s1 else self.max_val
            max_left_2 = nums2[idx2] if idx2 >= 0 else self.min_val
            min_right_2 = nums2[idx2 + 1] if (idx2 + 1) < s2 else self.max_val

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if total % 2:
                    # odd
                    return min(min_right_1, min_right_2)
                # even
                return (
                    min(min_right_1, min_right_2)
                    + max(max_left_1, max_left_2)
                ) / 2

            if max_left_1 > min_right_2:
                right = idx1 - 1
            else:
                left = idx1 + 1
