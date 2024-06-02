# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_idx = 0
        for i in range(len(arr)):
            if abs(x-arr[closest_idx]) > abs(x-arr[i]):
                closest_idx = i
        
        ans = []
        n = len(arr)
        l, r = closest_idx-1, closest_idx

        # picking the next closest each time, starting from the idx of closest we found. We spread out from the closest. it works since the arr is sorted
        while len(ans) != k: #this works well because 1 <= k <= arr.length
            dist_l = abs(x-arr[l]) if l >= 0 else float('Inf')
            dist_r = abs(x-arr[r]) if r < n else float('Inf')

            if dist_r < dist_l:
                ans.append(arr[r])
                r += 1
            else:
                ans.insert(0, arr[l])
                l -= 1
        
        return ans
