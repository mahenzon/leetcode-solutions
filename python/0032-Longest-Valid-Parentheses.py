class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # we need a non-empty stack from the start
        stack = [-1]
        count = 0
        for idx, c in enumerate(s):
            if c == "(":
                # if new p. is opened, just save its index
                stack.append(idx)
            elif len(stack) == 1:
                # if p. is closed, but we don't have any opened p.
                # (because len 1 is default)
                # set start idx to current (won't be included)
                stack[0] = idx
            else:
                # if p. is closed, pop open p.
                stack.pop()
                # and get diff between current and the one before last open
                count = max(count, idx - stack[-1])

        return count
