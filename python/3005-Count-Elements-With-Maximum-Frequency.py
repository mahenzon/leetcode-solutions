class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = [0] * 101
        max_freq = 0
        appeared_times = 0

        for num in nums:
            counts[num] += 1
            if counts[num] > max_freq:
                max_freq = counts[num]
                appeared_times = 1
            elif counts[num] == max_freq:
                appeared_times += 1

        return max_freq * appeared_times
