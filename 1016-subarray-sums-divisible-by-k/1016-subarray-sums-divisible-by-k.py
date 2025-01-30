class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        sums=0
        hm={0:1}
        for i in range(len(nums)):
            sums +=nums[i]
            reminder = sums %k
            if reminder<0:
                reminder +=k
            if reminder in hm:
                count +=hm[reminder]
                hm[reminder] +=1
            else:
                hm[reminder] = 1
        return count