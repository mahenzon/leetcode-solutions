class Solution:
    def totalMoney(self, n: int) -> int:
        week_days = 7
        # full weeks in `n`
        weeks = n // week_days
        # first week deposit
        # 1 + 2 + 3 + 4 + 5 + 6 + 7
        first_week_deposit = 28
        # last week deposit
        # subtract first week from the `weeks`
        # because it's added already
        last_week_deposit = first_week_deposit + week_days * (weeks - 1)

        # magic math for full weeks
        # The formula for the sum of a series from 1 to n is:
        # S = (n/2) * (1 + n)
        res = weeks * (last_week_deposit + first_week_deposit) // 2

        # what if n has extra days (not full week)
        extra_days = n % 7
        monday_deposit = weeks + 1
        last_day_deposit = monday_deposit + extra_days - 1
        # S = (y - x + 1) / 2 ) * (x + y)
        res += (
            (last_day_deposit + monday_deposit)
            * (last_day_deposit - monday_deposit + 1)
            // 2
        )

        return res
