class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMax=[0]*n
        leftMax[0]=height[0]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
            
        rightMax=[0]*n
        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])

        trapped=0
        for i in range(n):
            trapped +=min(leftMax[i],rightMax[i])-height[i]
        return trapped