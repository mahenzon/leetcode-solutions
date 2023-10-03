class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        nums_count = {}

        for num in nums:
            if num in nums_count:
                # if there's only one num,
                #   you can build one pair
                # if there're two same nums already,
                #   you can build two more pairs
                res += nums_count[num]
                # don't forget to increase count
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        return res
