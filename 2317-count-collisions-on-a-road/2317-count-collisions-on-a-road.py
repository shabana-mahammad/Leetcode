class Solution:
    def countCollisions(self, directions: str) -> int:
        right=0
        stable=0
        ans=0
        for i in directions:
            if i == "R": 
                right +=1
            if i == "S":
                ans +=right
                stable=1
                right =0
            if i == "L":
                if right>0:
                    ans +=right + 1
                    stable = 1
                    right = 0
                elif stable:
                    ans +=1 
        return ans