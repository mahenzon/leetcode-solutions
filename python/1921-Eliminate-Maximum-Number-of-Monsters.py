class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        arrival_times = sorted([
            distance / monster_speed
            for distance, monster_speed in zip(dist, speed)
        ])
        for step, arrival_time in enumerate(arrival_times):
            if step >= arrival_time:
                return step
        return len(dist)
