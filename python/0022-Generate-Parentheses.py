class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.n = n
        self.stack = []
        self.res = []

        self.backtrack(0, 0)
        return self.res

    def backtrack(self, opened, closed):
        if opened == closed == self.n:
            self.res.append("".join(self.stack))
            return

        if opened < self.n:
            self.stack.append("(")
            self.backtrack(opened + 1, closed)
            self.stack.pop()

        if closed < opened:
            self.stack.append(")")
            self.backtrack(opened, closed + 1)
            self.stack.pop()
