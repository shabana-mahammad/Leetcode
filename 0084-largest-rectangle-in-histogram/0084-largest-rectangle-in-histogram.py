class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ns=[len(heights)]*len(heights)
        ps=[-1]*len(heights)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                ns[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                ps[i]=stack[-1]
            stack.append(i)
        maxi=0
        for i in range(len(heights)):
            maxi=max(maxi,(ns[i]-ps[i]-1)*heights[i])
        return maxi

        