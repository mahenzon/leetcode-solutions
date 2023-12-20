class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = 101
        b = 101

        for price in prices:
            if price < a:
                a, b = price, a
            elif price < b:
                b = price

        if (remainder := money - a - b) >= 0:
            return remainder

        return money
