# https://leetcode.com/problems/asteroid-collision/description/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            if not st or ast>=0:
                st.append(ast)
            else: #negative 
                abs_ast = abs(ast)
                #check >=0 since ast moving in same direction do not collide
                while st and st[-1] >= 0 and abs_ast > st[-1]:
                    st.pop()
                if not st or st[-1] < 0: #meaning, st was the largest and it destroyed all the positives
                    st.append(ast)
                elif st[-1] >= 0 and st[-1] == abs_ast: #check if absolute values are equal
                    st.pop()
        
        return st
