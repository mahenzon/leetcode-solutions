class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        for sandwich in sandwiches:
            if not counts[sandwich]:
                break
            counts[sandwich] -= 1

        return sum(counts)
