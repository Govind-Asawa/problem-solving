// https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution {
    public int firstUniqChar(String s) {
        char[] sarray = s.toCharArray();
        HashSet<Character> set = new HashSet<>();
        HashSet<Character> repeats = new HashSet<>();

        for(char c: sarray)
        {
            if(set.contains(c))
                repeats.add(c);
            set.add(c);
        }
        for (int i=0; i<sarray.length; i++)
            if (!repeats.contains(sarray[i]))
                return i;
        return -1;
    }
}
