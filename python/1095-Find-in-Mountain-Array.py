# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def find_mountain_peak(self) -> int:
        left = 1
        right = self.arr_len - 2

        while left <= right:
            mid = left + (right - left) // 2
            val_left = self.arr.get(mid - 1)
            val_mid = self.arr.get(mid)
            val_right = self.arr.get(mid + 1)
            if val_left < val_mid < val_right:
                left = mid + 1
            elif val_left > val_mid > val_right:
                right = mid - 1
            else:
                return mid

    def bin_search(self, start: int, end: int, asc=True) -> int:
        """
        asc = True
        # sorted ascending: [1, 3, 6, ...]

        asc = False => desc = True
        # sorted descending: [7, 4, 2, ...]
        """
        left = start
        right = end

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.arr.get(mid)
            if mid_value == self.target:
                return mid

            if mid_value > self.target:
                if asc:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid_value < self.target:
                if asc:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # equals
                return mid

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.arr = mountain_arr
        self.arr_len = self.arr.length()
        self.target = target
        peak = self.find_mountain_peak()
        if peak is None:
            return -1

        result = self.bin_search(0, peak, asc=True)
        if result is not None:
            return result

        result = self.bin_search(peak, self.arr_len - 1, asc=False)
        if result is not None:
            return result

        return -1
