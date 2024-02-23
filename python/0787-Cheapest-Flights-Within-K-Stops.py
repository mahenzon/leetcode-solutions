class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices: list[int | None] = [None] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp_prices = prices.copy()

            for source, destination, price in flights:
                src_price = prices[source]
                if src_price is None:
                    continue
                dest_price = temp_prices[destination]
                if dest_price is None or src_price + price < temp_prices[destination]:
                    temp_prices[destination] = src_price + price
            prices = temp_prices

        return prices[dst] or -1
