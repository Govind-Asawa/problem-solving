# https://www.geeksforgeeks.org/problems/rotation4723/1
class Solution {
    int findKRotation(int arr[], int n) {
        int low = 0, high = n-1;
        int minidx = 0;
        while (low <= high)
        {
            int mid = low + (high - low)/2;
           
            //check if the left half is sorted
            if (arr[low] <= arr[mid])
            {
                if (arr[low] <= arr[minidx])
                    minidx = low;
                low = mid+1;
            }
            else
            {
                if (arr[mid] <= arr[minidx])
                    minidx = mid;
                
                high = mid-1;
            }
        }
        return minidx;
    }
}
