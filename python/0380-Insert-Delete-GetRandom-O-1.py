# `random` is already imported in LeetCode
import random


class RandomizedSet:

    def __init__(self):
        # all values
        self.values_list = []
        # value to index
        self.values_map = {}

    def insert(self, val: int) -> bool:
        if val in self.values_map:
            return False

        idx = len(self.values_list)
        self.values_list.append(val)
        self.values_map[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_map:
            return False
        idx = self.values_map.pop(val)
        last_val = self.values_list.pop()
        if idx < len(self.values_list):
            self.values_list[idx] = last_val
            self.values_map[last_val] = idx
        return True

    def getRandom(self) -> int:
        return random.choice(self.values_list)
