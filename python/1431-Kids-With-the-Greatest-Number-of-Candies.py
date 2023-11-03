class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for i, count in enumerate(candies):
            candies[i] = count + extraCandies >= max_candies
        return candies
