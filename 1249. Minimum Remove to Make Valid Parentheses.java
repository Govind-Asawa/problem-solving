# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
import java.util.*;
class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Element> st = new Stack<>();
        int i = 0;

        StringBuilder sb = new StringBuilder(s);
        while( i < sb.length())
        {
            char c = sb.charAt(i);
            if (c == ')' && st.isEmpty())
            {
                sb.deleteCharAt(i);
                continue;
            }
            else if (c == ')')
                st.pop();
            else if(c == '(')
                st.push(new Element('(', i));

            i++;
        }

        while (!st.isEmpty())
        {
            Element e = st.pop();
            sb.deleteCharAt(e.idx);
        }

        return sb.toString();
    }
}
class Element{
    char c;
    int idx;
    Element(char c, int i)
    {
        this.c = c;
        this.idx = i;
    }
}
