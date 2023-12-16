class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[-1] - arr[0]
        result = []
        for idx in range(len(arr) - 1):
            diff = arr[idx + 1] - arr[idx]
            if diff < min_diff:
                min_diff = diff
                result = []
            if diff == min_diff:
                result.append((arr[idx], arr[idx + 1]))

        return result
