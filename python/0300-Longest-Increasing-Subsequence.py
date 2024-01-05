# O(n^2) solution (Dynamic Programming)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)

        for cur_idx in range(len(nums) - 1, -1, -1):
            for next_idx in range(cur_idx + 1, len(nums)):
                if nums[cur_idx] < nums[next_idx]:
                    lengths[cur_idx] = max(lengths[cur_idx], 1 + lengths[next_idx])

        return max(lengths)


# O(n*logn) solution (Binary Search)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        seq.append(nums[0])

        for num in nums:
            if num > seq[-1]:
                seq.append(num)
            else:
                seq[bisect.bisect_left(seq, num)] = num

        return len(seq)
