class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS = len(img)
        COLS = len(img[0])

        for r in range(ROWS):
            for c in range(COLS):
                total = 0
                count = 0

                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (
                            i < 0 or i >= ROWS
                            or j < 0 or j >= COLS
                        ):
                            continue
                        total += img[i][j] % 256
                        count += 1

                # math magic + bits manipulation magic
                img[r][c] ^= (total // count) << 8

        for r in range(ROWS):
            for c in range(COLS):
                img[r][c] >>= 8

        return img
