class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        provinces=0
        for i in range(n):
            if not visited[i]:
                provinces +=1 
                self.dfs(i, isConnected, visited)
        return provinces

    def dfs(self, i, isConnected, visited):
        visited[i]=True
        for j in range(len(isConnected)):
            if isConnected[i][j] and not visited[j]:
                self.dfs(j, isConnected, visited)