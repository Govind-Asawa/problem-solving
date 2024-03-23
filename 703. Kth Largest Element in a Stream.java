https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import java.util.PriorityQueue;
class KthLargest {
    PriorityQueue<Integer> minHeap = null;
    int k = 0;
    public KthLargest(int k, int[] nums) {
        this.minHeap = new PriorityQueue<>(k, (a,b) -> a-b);
        this.k = k;
        for(int num : nums)
            this.add(num);
    }
    
    public int add(int val) {
        if(this.minHeap.size() < this.k )
            minHeap.add(val);

        else if (this.minHeap.peek() <= val)
        {
            this.minHeap.poll(); //remove kth largest so far
            this.minHeap.add(val); 
        }

        return this.minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
