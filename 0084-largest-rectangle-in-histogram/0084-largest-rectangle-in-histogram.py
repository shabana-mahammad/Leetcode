class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[0]*len(heights)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                left[i]=0
            else:
                left[i]=stack[-1]+1            
            stack.append(i)
        right=[0]*len(heights)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                right[i]=len(heights)-1
            else:
                right[i]=stack[-1]-1
            stack.append(i)
        max_area=0
        for i in range(len(heights)):
            if (right[i]-left[i]+1)*heights[i] > max_area:
                max_area=(right[i]-left[i]+1)*heights[i]
        return max_area

        