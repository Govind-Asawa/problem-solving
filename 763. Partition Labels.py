# https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0,0
        parts = []

        lastOcc = {}
        for i, val in enumerate(s):
            lastOcc[val] = i

        for curr in range(len(s)):
            end = max(lastOcc[s[curr]], end)
            if curr == end:
                parts.append(end-start+1)
                start = end+1

        return parts
