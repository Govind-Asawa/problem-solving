# https://leetcode.com/problems/hand-of-straights/description/
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        count = Counter(hand)
        handc = sorted(hand) #since every new group will start from the smallest

        for val in handc:
            #meaning already included in some group
            if not count[val]:
                continue
            count[val] -= 1
            for i in range(1,groupSize):
                # No seq found that should start with val
                if not count[val+i]:
                    return False
                count[val+i] -= 1

        return True
