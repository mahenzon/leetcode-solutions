class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []

        for c in s:
            if c in open_to_close:
                if not (
                    stack
                    and (stack.pop() == open_to_close[c])
                ):
                    return False
            else:
                stack.append(c)

        return not stack
