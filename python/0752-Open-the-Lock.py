# `collections` is already imported in LeetCode
import collections


class Solution:
    def next_locks(self, lock: tuple[int, ...]) -> Sequence[tuple[int, ...]]:
        lock = list(lock)
        res = []
        for idx, val in enumerate(lock):
            lock[idx] = (val + 1) % 10
            res.append(tuple(lock))
            lock[idx] = (val - 1 + 10) % 10
            res.append(tuple(lock))
            lock[idx] = val
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        start = (0, 0, 0, 0)
        visited = {
            tuple(map(int, d))
            for d in deadends
        }
        if start in visited:
            # if is dead end on start
            return -1
        visited.add(start)
        target = tuple(map(int, target))
        q = collections.deque()
        q.append(start)
        step = 0
        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return step
                for new_lock in self.next_locks(lock):
                    if new_lock not in visited:
                        visited.add(new_lock)
                        q.append(new_lock)
            step += 1

        return -1
