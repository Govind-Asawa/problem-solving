// https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        Arrays.stream(nums).forEach(num -> set.add(num));
        int maxCount = 0;

        for(int num: nums)
        {
            if(set.contains(num-1))
                continue;
            int count = 0;
            while(set.contains(num+count))
                count++;

            maxCount = Math.max(maxCount, count);
        }
        return maxCount;

    }
}
