# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
class Solution:
    def maxProduct(self, s: str) -> int:
        palins = {}
        n = len(s)

        for mask in range(1,pow(2,n)):
            i = 0
            subseq = ''
            for i in range(n):
                if mask & (1 << i):
                    subseq = s[i] + subseq
            if subseq == subseq[::-1]:
                palins[mask] = len(subseq)

        maxprd = 0

        for m1 in palins.keys():
            for m2 in palins.keys():
                if not m1 & m2:
                    maxprd = max(maxprd, palins[m1]*palins[m2])

        return maxprd
