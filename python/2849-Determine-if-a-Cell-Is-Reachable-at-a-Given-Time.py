class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        move_x = abs(sx - fx)
        move_y = abs(sy - fy)
        if move_x == 0 and move_y == 0 and t == 1:
            return False
        return t >= max(move_x, move_y)
