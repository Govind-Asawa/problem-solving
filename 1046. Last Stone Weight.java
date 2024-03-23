# https://leetcode.com/problems/last-stone-weight/
import java.util.PriorityQueue;
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(stones.length, (a,b) -> b-a);

        for (int stone: stones)
            maxHeap.add(stone);

        while(maxHeap.size() > 1)
        {
            int first = maxHeap.poll();
            int second = maxHeap.poll();

            if(first == second)
                continue;
            
            maxHeap.add(first-second);
        }

        return maxHeap.size() == 1 ? maxHeap.poll() : 0;
    }
}
