from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        directions=[(-1,0),(1,0),(0,1),(0,-1)] 
        queue=deque()
        result=[[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    result[i][j]=0
                    queue.append((i,j))
        while queue:
            i,j=queue.popleft()
            for dx,dy in directions:
                new_i=i+dx
                new_j=j+dy
                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and result[new_i][new_j]==-1:
                    result[new_i][new_j]=result[i][j]+1 
                    queue.append(([new_i,new_j]))
        return result
