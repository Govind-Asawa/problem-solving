# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)} # [cost, i]

        # creating adj list, doing just bcoz not already given
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        mincost = 0
        visit = set()
        minheap = [[0,0]] # [cost, i] -- uses the first index i.e., cost to create minHeap
        
        # prim's algo to find MST
        while len(visit) < n:
            cost, u = heapq.heappop(minheap)
            if u in visit:
                continue
            
            visit.add(u)
            mincost += cost

            for vCost, v in adj[u]: #look at neigh edges, include those that connect it with unvisited vertices
                if v not in visit:
                    heapq.heappush(minheap, [vCost, v])
        
        return mincost
