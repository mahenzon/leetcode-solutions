class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair [ temp, idx ]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append([temp, i])

        return res
