# https://leetcode.com/problems/course-schedule/description/
# simple optimization is to count the number of courses getting completed
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nBefore = [0]*numCourses #number of courses that needs to be completed before taking ith course
        allAfter = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            nBefore[after] += 1
            allAfter[before].append(after)
        
        q = []
        for i in range(numCourses):
            if nBefore[i] == 0:
                q.append(i)

        while q:
            course = q.pop(0)
            for after in allAfter[course]:
                nBefore[after] -= 1
                if nBefore[after] == 0: # if it has no more dependencies
                    q.append(after)

        return True if not list(filter(lambda x: x, nBefore)) else False
