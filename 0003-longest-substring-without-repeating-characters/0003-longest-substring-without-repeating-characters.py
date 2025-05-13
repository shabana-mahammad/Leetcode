class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        i=0
        j=0
        ans=0
        while j<len(s):
            if s[j] not in sett:
                sett.add(s[j])
                ans=max(ans,j-i+1)
                j +=1
            else:
                sett.remove(s[i])
                i +=1
        return ans
