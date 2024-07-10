class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            match log:
                case "./":
                    pass
                case "../":
                    if level:
                        level -= 1
                case _:
                    level += 1
        return level
