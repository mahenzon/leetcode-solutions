class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                count10 += 1
                count5 -= 1
            else:
                if count10:
                    count10 -= 1
                    count5 -= 1
                else:
                    count5 -= 3

            if count5 < 0:
                return False

        return True
