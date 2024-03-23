// https://leetcode.com/problems/k-closest-points-to-origin/description/
import java.util.PriorityQueue;
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> maxHeap = new PriorityQueue<>(k, (p1,p2) -> p2.d - p1.d);
        int[][] ans = new int[k][2];

        for(int[] pt : points)
        {
            Point p = new Point(pt[0], pt[1]);
            if(maxHeap.size() < k)
                maxHeap.add(p);

            //found a point closer than the kth closest point
            else if(maxHeap.peek().d >= p.d)
            {
                maxHeap.poll();//remove farthest so far
                maxHeap.add(p);
            }
        }

        for(int i=0;i<k;i++)
        {
            Point p = maxHeap.poll();
            ans[i] = new int[]{p.x, p.y};
        }
        
        return ans;
    }
}

class Point
{
    int x, y, d;
    Point(int x, int y)
    {
        this.x = x;
        this.y = y;
        this.d = x*x + y*y;
    }
}
