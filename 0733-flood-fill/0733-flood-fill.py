from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(sr, sc)])
        originalcolor=image[sr][sc]
        if originalcolor==color: 
            return image 

        while queue:
            i,j=queue.popleft()
            image[i][j]=color
            for dx,dy in directions: 
                new_i,new_j= i+dx, j+dy
                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and image[new_i][new_j]==originalcolor:
                    queue.append((new_i,new_j))
        return image