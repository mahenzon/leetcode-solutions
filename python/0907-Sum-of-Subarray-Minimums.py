class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        stack = []
        N = len(arr)
        arr.append(-1)
        for idx, val in enumerate(arr):
            while stack and arr[stack[-1]] >= val:
                prev_idx = stack.pop()
                prev_val = arr[prev_idx]

                left = -1
                if stack:
                    left = stack[-1]
                count = (prev_idx - left) * (idx - prev_idx)
                res += prev_val * count

            stack.append(idx)

        return res % mod
