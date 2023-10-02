class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_dominance = 0

        # if there're 3 same colors in a row,
        # it's +1 point for one of the players
        # Alice wins if she has higher score than Bob
        # if score is the same, Bob wins
        for idx in range(1, len(colors) - 1):
            if colors[idx - 1] == colors[idx] == colors[idx + 1]:
                if colors[idx] == 'A':
                    alice_dominance += 1
                else:
                    alice_dominance -= 1

        return alice_dominance > 0
