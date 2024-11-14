class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm={0:1}
        sums=0
        cnt=0
        for i in range(len(nums)):
            sums +=nums[i]
            required=sums-k
            if required in hm:
                cnt +=hm[required]
            if sums in hm:
                hm[sums] +=1
            else:    
                 hm[sums] = 1 
        return cnt