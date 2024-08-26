// https://leetcode.com/problems/top-k-frequent-elements/

import java.util.*;
class Solution {
    class Point 
    {
        int num, count;
        Point(int num, int count)
        {
            this.num = num;
            this.count = count;
        }
        int getNum()
        {
            return num;
        }
    }
    public int[] topKFrequent(int[] nums, int k) {
        //creating a max-heap
        PriorityQueue<Point> heap = new PriorityQueue<>((v1, v2) -> v2.count - v1.count);
        HashMap<Integer, Integer> map = new HashMap<>();

        //count the occurances
        Arrays.stream(nums).forEach(num -> map.put(num, map.getOrDefault(num, 0)+1));
        // create a Point for each occurance
        map.entrySet().stream().forEach(e -> heap.add(new Point(e.getKey(), e.getValue())));

        int[] res = new int[k];
        for (int i=0;i<k;i++)
            res[i] = heap.poll().getNum(); //The top-most value will contain num with highest count

        return res;
    }
}
