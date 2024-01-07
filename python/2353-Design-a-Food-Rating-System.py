# If you're OK with importing SortedSet:
from sortedcontainers import SortedSet


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foods = {}
        self.cuisines = defaultdict(SortedSet)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisines[cuisine].add((-rating, food))
            self.foods[food] = (cuisine, rating)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foods[food]

        self.cuisines[cuisine].remove((-rating, food))
        self.cuisines[cuisine].add((-newRating, food))

        self.foods[food] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]


# `defaultdict` and `bisect` helpers are already imported in LeetCode
from collections import defaultdict
from bisect import bisect_left, insort


# using bisect (slower because of O(n) time for .pop and .insert (insort)
class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foods = {}
        self.cuisines = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            insort(self.cuisines[cuisine], (-rating, food))
            self.foods[food] = (cuisine, rating)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foods[food]

        idx = bisect_left(self.cuisines[cuisine], (-rating, food))
        self.cuisines[cuisine].pop(idx)
        insort(self.cuisines[cuisine], (-newRating, food))

        self.foods[food] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]
