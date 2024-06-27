class Solution:
    def build(self, left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return

        mid = left + (right - left) // 2
        return TreeNode(
            self.nums[mid],
            self.build(left, mid - 1),
            self.build(mid + 1, right),
        )

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.build(0, len(nums) - 1)
