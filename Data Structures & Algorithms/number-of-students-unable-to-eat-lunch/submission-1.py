class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        remaining = len(students)
            

        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break

            counts[sandwich] -= 1
            remaining -= 1
        return remaining
