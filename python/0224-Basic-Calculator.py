class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        prev_sign = 1
        sign_stack = [prev_sign]

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                sign_stack.append(prev_sign)
            elif c == ")":
                sign_stack.pop()
            elif c in "+-":
                res += prev_sign * num
                prev_sign = (1 if c == "+" else -1) * sign_stack[-1]
                num = 0

        res += prev_sign * num
        return res
