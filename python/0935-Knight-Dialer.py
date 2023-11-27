class Solution:
    mod = 10 ** 9 + 7
    paths = [
        (4, 6),     # 0
        (6, 8),     # 1
        (7, 9),     # 2
        (4, 8),     # 3
        (0, 3, 9),  # 4
        (),         # 5
        (0, 1, 7),  # 6
        (2, 6),     # 7
        (1, 3),     # 8
        (2, 4),     # 9
    ]

    def knightDialer(self, n: int) -> int:
        count = len(self.paths)
        all_moves = [1] * count
        for _ in range(1, n):
            next_moves = [0] * count
            for idx, moves in enumerate(self.paths):
                for move in moves:
                    next_moves[move] = (next_moves[move] + all_moves[idx]) % self.mod
            all_moves = next_moves

        return sum(all_moves) % self.mod
