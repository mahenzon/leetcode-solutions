class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            cnt = cnt + 1 if num % 2 else 0
            if cnt == 3:
                return True

        return False
