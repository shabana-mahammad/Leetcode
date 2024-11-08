class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n=len(positions)
        ids=list(range(n))
        ids.sort(key=lambda i: positions[i])
        stack=[]
        for id in ids:
            if directions[id]=="R":
                stack.append(id)
            else:
                while stack and healths[id]>0:
                    if healths[id]>healths[stack[-1]]:
                        healths[id] -=1
                        healths[stack.pop()]=0
                    elif healths[id] < healths[stack[-1]]:
                        healths[id]=0
                        healths[stack[-1]] -=1
                    else:
                        healths[id]=0
                        healths[stack.pop()]=0
                        
        ans=[]
        for i in healths:
            if i>0:
                ans.append(i)
        return ans
