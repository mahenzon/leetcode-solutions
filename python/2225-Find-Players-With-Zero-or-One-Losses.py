class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_loss = []
        one_loss = []
        result = [no_loss, one_loss]

        loses = {}

        for winner, loser in matches:
            if winner not in loses:
                loses[winner] = 0
            # this person lost a match one more times
            loses[loser] = 1 + loses.get(loser, 0)

        for person, loose_times in loses.items():
            if loose_times < 2:
                # 0 or 1
                result[loose_times].append(person)

        no_loss.sort()
        one_loss.sort()
        return result
