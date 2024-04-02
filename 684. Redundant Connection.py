# https://leetcode.com/problems/redundant-connection/description/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        for u, v in edges:
            pu = self.find(u, parent)
            pv = self.find(v, parent)

            if pu == pv:
                return [u,v]
            
            self.union(pu,pv,parent)
        
        return []

    def find(self, u, parent):
        if u == parent[u]:
            return u

        return self.find(parent[u], parent)

    def union(self, u, v, parent):
        parent[v] = u  
