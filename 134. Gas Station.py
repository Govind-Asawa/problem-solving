# https://leetcode.com/problems/gas-station/description/
# https://youtu.be/lJwbPZGo05A

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = []
        for gasVal, costVal in zip(gas, cost):
            diff.append(gasVal - costVal)

        cumgas = idx = 0
        for i in range(len(gas)):
            cumgas += diff[i]
            if cumgas < 0:
                cumgas = 0
                idx = i+1
        
        return idx

