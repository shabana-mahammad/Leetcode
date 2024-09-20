class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(asteroids[i]) 
                elif stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
        return stack