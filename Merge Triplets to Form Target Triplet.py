# 
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        isPossible = set()
        
        for triplet in triplets:
            # Since triplets with val > target are of no use
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(len(target)):
                if triplet[i] == target[i]:
                    isPossible.add(i)

        return len(isPossible) == 3
