class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        q = n // 4

        for i in range(n - q):
            if arr[i] == arr[i + q]:
                return arr[i]
