# https://leetcode.com/problems/remove-k-digits/description/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        num += "0" 
        #this will help if we have something like "23456" the while loop will not remove any
        #so, if we have 0 at the end, the loop will work perfect

        ls = list(num)

        i = 0
        while (i < len(ls)-1) and k > 0:
            if ls[i] > ls[i+1]:
                ls.pop(i)
                k -= 1
                if i != 0:
                    i -= 1
            else:
                i += 1

        ls.pop() #remove the 0 we've added
        
        i = 0
        while i < len(ls)-1 and ls[i] == '0':
            i += 1
        
        return ''.join(ls[i:])
