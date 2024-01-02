class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = {}
        res = []
        for num in nums:
            cnt = count.get(num, 0)
            if len(res) == cnt:
                res.append([])
            res[cnt].append(num)
            count[num] = cnt + 1
        return res
