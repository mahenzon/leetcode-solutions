# `collections` and `random` are already imported in LeetCode
import collections
import random


class RandomizedCollection:

    def __init__(self):
        self.values_list = []
        self.values_map = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        not_present = not self.values_map[val]
        idx = len(self.values_list)
        self.values_list.append(val)
        self.values_map[val].add(idx)
        return not_present

    def remove(self, val: int) -> bool:
        if not self.values_map[val]:
            return False

        val_idx = next(iter(self.values_map[val]))
        self.values_map[val].remove(val_idx)
        last_val = self.values_list.pop()
        last_val_idx = len(self.values_list)
        if val_idx < len(self.values_list):
            self.values_list[val_idx] = last_val
            self.values_map[last_val].remove(last_val_idx)
            self.values_map[last_val].add(val_idx)

        return True

    def getRandom(self) -> int:
        return random.choice(self.values_list)
