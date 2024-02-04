class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1]:
                candies[idx] = candies[idx - 1] + 1

        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

        return sum(candies)
