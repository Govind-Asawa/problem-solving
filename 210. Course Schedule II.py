# https://leetcode.com/problems/course-schedule-ii/description/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nBefore = [0]*numCourses #number of courses that needs to be completed before taking ith course
        allAfter = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            nBefore[after] += 1
            allAfter[before].append(after)
        
        q = []
        ans = []
        for i in range(numCourses):
            if nBefore[i] == 0:
                q.append(i)

        while q:
            course = q.pop(0)
            ans.append(course)
            for after in allAfter[course]:
                nBefore[after] -= 1
                if nBefore[after] == 0: # if it has no more dependencies
                    q.append(after)

        return [] if len(ans) != numCourses else ans
