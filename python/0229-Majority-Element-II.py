class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if len(cache) > 2:
                for num, count in list(cache.items()):
                    if count == 1:
                        cache.pop(num)
                    else:
                        cache[num] = count - 1

        third = len(nums) // 3
        res = []
        for num in cache:
            if nums.count(num) > third:
                res.append(num)
        return res
