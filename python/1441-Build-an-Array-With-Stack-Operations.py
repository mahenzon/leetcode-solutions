class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        actions = []

        stream_value = 0
        for elem in target:
            while stream_value < elem:
                stream_value += 1
                actions.extend(["Push", "Pop"])
            else:
                actions.pop()

        return actions
