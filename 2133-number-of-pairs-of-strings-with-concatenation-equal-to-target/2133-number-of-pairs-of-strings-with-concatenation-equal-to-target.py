from collections import defaultdict
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        mp= defaultdict(int)
        count =0
        for num in nums:
            mp[str(num)] +=1
        target_str=str(target)
        for i in range(1,len(target_str)):
            first = target_str[:i]
            second = target_str[i:]
            if first==second:
                count += (mp[first])*(mp[second]-1)
            else:
                count += mp[first]*mp[second]
        return count
