class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (index, height)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                prev_index, prev_height = stack.pop()
                max_area = max(
                    max_area, prev_height * (index - prev_index))
                start = prev_index
            stack.append((start, height))

        for index, height in stack:
            max_area = max(
                max_area, height * (len(heights) - index))

        return max_area
