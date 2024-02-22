class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        # 0 idx is not used
        trusts[0] = -1
        # exclude the judge
        target_trusts = n - 1
        for outgoing, incoming in trust:
            trusts[outgoing] -= 1
            trusts[incoming] += 1

        for idx, trusts_count in enumerate(trusts):
            if trusts_count == target_trusts:
                return idx

        return -1
