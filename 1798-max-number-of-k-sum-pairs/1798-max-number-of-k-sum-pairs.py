class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hm={}
        count=0
        for i in range(len(nums)):
            required = k-nums[i]
            if required in hm and hm[required]>0:
                count +=1 
                hm[required] -=1
            else:
                hm[nums[i]] = hm.get(nums[i],0)+1
        return count