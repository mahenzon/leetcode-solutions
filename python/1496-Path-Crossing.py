class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = (0, 0)
        visited = {point}

        paths = {
            # (x, y)
            "E": (1, 0),
            "W": (-1, 0),
            "N": (0, 1),
            "S": (0, -1),
        }
        for p in path:
            x, y = paths[p]
            point = point[0] + x, point[1] + y
            if point in visited:
                return True
            visited.add(point)

        return False
