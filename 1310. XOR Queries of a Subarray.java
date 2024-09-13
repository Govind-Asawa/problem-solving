// https://leetcode.com/problems/xor-queries-of-a-subarray/description
/*
XOR properties

A ^ 0 = A
A ^ A = 0
*/

class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] leftxors = new int[arr.length];
        int prev = 0;
        for (int i=0;i<arr.length;i++)
        {
            leftxors[i] = prev ^ arr[i];
            prev = leftxors[i];
        }

        int[] result = new int[queries.length];
        int currIdx = 0;
        for (int[] query : queries)
        {
            int i = query[0], j = query[1];
            result[currIdx++] = arr[i]^leftxors[i]^leftxors[j];
        }
        return result;
    }
}
