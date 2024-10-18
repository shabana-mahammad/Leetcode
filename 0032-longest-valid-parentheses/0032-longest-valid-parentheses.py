class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        mp={'(':')'}
        maxl=0
        for idx,char in enumerate(s):
            if char in mp:
                stack.append(idx)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(idx)

                length=idx-stack[-1]
                if length>maxl:
                    maxl=length
        return maxl
        