class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed_last_idx = len(flowerbed) - 1

        for idx, val in enumerate(flowerbed):
            if val:
                continue

            # check left: idx is not first and prev val is not empty
            if idx and flowerbed[idx - 1]:
                continue

            # check right: idx is not last and next val is not empty
            if idx != flowerbed_last_idx and flowerbed[idx + 1]:
                continue

            count += 1
            # mark this plot as occupied
            flowerbed[idx] = 1

        return count >= n
