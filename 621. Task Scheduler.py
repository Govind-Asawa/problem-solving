# https://leetcode.com/problems/task-scheduler/description/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        #we actually want maxHeap but since python provides min, we insert -1*val in minheap, which makes it a max heap
        minHeap = [-cnt for cnt in counts.values()] 
        heapq.heapify(minHeap)

        q = deque() # [-cnt, time]
        time = 0

        while minHeap or q:
            time += 1

            if minHeap:
                cnt = heapq.heappop(minHeap)
                cnt += 1 # we are using this, so reduce the frequency. We add since our cnt is -ve
                if cnt:
                    q.append([cnt, time + n]) #we store when can we use it again
            
            if q and q[0][1] == time: #if we have something that can be used next
                heapq.heappush(minHeap, q.popleft()[0]) #we only need count

        return time
