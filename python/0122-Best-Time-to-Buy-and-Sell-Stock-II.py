class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last_price = prices[0]
        for price in prices:
            if price > last_price:
                profit += price - last_price
            last_price = price

        return profit
