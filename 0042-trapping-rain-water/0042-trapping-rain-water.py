class Solution:
    def trap(self, height: List[int]) -> int:
        maxL=[]
        maxleft=0
        for i in range(len(height)):
            maxL.append(maxleft)
            maxleft=max(maxleft,height[i])
        print(maxL)
        maxR=[]
        maxright=0
        for i in range(len(height)-1,-1,-1):
            maxR.append(maxright)
            maxright=max(maxright,height[i])
        maxR=maxR[::-1]
        print(maxR)
        total_water=0
        for i in range(len(height)):
            val=min(maxL[i],maxR[i])-height[i]
            if val>0:
                total_water +=val
        return total_water
        