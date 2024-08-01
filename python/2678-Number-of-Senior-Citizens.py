class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # short:
        # return sum(int(d[-4:-2]) > 60 for d in details)

        # performant:
        return sum(d[-4] >= '7' or d[-4] == '6' and d[-3] != '0' for d in details)
