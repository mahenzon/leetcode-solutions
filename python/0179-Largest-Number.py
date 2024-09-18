class StringPairComparator(str):
    def __lt__(a: str, b: str) -> bool:
        return a + b > b + a


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str, nums), key=StringPairComparator)).lstrip("0") or "0"
