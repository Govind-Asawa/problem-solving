# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        for i in range(len(students)):
            available = sandwiches[i]
            if not count[available]: # everyone goes home if no one wants to eat whats available on the top
                return len(students) - i
            count[available] -= 1

        return 0
