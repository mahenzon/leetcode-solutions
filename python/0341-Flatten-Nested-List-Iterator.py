# `collections` is already imported in LeetCode
import collections

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# is there a way to solve it in O(1) by memory?


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        # you could fill a regular list and then reverse it at the end
        self.integers = collections.deque()
        self.flatten(nestedList)

    def flatten(self, integers: list[NestedInteger]):
        for elem in integers:
            if elem.isInteger():
                self.integers.append(elem.getInteger())
            else:
                self.flatten(elem.getList())

    def next(self) -> int:
        return self.integers.popleft()

    def hasNext(self) -> bool:
        return len(self.integers) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
