class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleets = 0
        slowest_car_time_to_dest = 0
        for start, speed in cars:
            current_car_time_to_dest = (target - start) / speed
            if slowest_car_time_to_dest < current_car_time_to_dest:
                fleets += 1
                slowest_car_time_to_dest = current_car_time_to_dest

        return fleets
