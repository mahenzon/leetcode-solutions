class MyQueue:

    def __init__(self):
        self.bottom = []
        self.top = []

    def push(self, x: int) -> None:
        self.bottom.append(x)

    def pop(self) -> int:
        self.fill()
        return self.top.pop()

    def peek(self) -> int:
        self.fill()
        return self.top[-1]

    def empty(self) -> bool:
        return not self.bottom and not self.top

    def fill(self) -> None:
        if not self.top:
            while self.bottom:
                self.top.append(self.bottom.pop())
