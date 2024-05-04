class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            remaining = limit - people[right]
            right -= 1
            if people[left] <= remaining:
                left += 1
            res += 1

        return res
