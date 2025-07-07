from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque()
        fresh_count=0
        for i in range(m):
            for j in range(n): 
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1: 
                    fresh_count +=1 
        if fresh_count==0:
            return 0

        minutes=0
        while queue:
            for _ in range(len(queue)):
                i,j=queue.popleft() 
                for dx,dy in directions: 
                    new_i,new_j= i+dx, j+dy 
                    if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j]==1:
                        grid[new_i][new_j]=2
                        queue.append((new_i,new_j))
                        fresh_count -=1 
            minutes +=1 
        return minutes-1 if fresh_count == 0 else -1
