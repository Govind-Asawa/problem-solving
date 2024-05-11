# https://leetcode.com/problems/validate-stack-sequences/description/
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        already_pushed = set()
        st = []
        last_pushed_idx = -1

        for popval in popped:
            if popval not in already_pushed: #go ahead and push it
                last_pushed_idx += 1
                while pushed[last_pushed_idx] != popval:
                    already_pushed.add(pushed[last_pushed_idx])
                    st.append(pushed[last_pushed_idx])
                    last_pushed_idx += 1
            elif st[-1] != popval:# if already pushed, it should be on top of the stack
                return False
            else:
                st.pop()

        return True
