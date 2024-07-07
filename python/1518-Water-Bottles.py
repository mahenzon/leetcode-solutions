class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # initial bottles + exchanged bottles
        return numBottles + (numBottles - 1) // (numExchange - 1)
