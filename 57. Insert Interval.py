class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        ans = []
        newIntl = newInterval

        for intl in intervals:
            #since ascending, if end < start of next, no chances of further overlap
            if newIntl[1] < intl[0]:
                break

            # if overlapping then merge
            if newIntl[0] <= intl[1] and newIntl[1] >= intl[0]:
                newIntl[0] = min(newIntl[0], intl[0])
                newIntl[1] = max(newIntl[1], intl[1])
            else:
                ans.append(intl)
            idx += 1

        ans.append(newIntl)
        if idx < len(intervals): #merge the left overs
            ans.extend(intervals[idx:])

        return ans
