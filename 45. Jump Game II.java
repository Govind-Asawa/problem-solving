// https://leetcode.com/problems/jump-game-ii/description/
/*
we wanna choose the best place to jump in the current jump range
the best place is that can take us the farthest
*/
class Solution {
    public int jump(int[] nums) {
        int jumps=0, stepsLeft = 0, n = nums.length;

        int maxIdx = -1;

        for (int i=0;i<n-1;i++)
        {
            //we wanna choose the loc from where we can jump the farthest
            if(maxIdx == -1 || maxIdx + nums[maxIdx] < i + nums[i] )
                maxIdx = i;

            if (stepsLeft == 0)
            {
                jumps++; //jumping to maxIdx
                stepsLeft = nums[maxIdx] - (i - maxIdx);
                maxIdx = -1;
            }
            stepsLeft--;
        }

        return jumps;
    }
}
