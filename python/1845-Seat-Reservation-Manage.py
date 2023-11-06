# `heapq` is already imported in LeetCode
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.available_seats = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.available_seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
