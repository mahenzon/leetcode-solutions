class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(
            "1" if num[idx] == "0" else "0"
            for idx, num in enumerate(nums)
        )
