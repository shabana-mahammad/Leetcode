class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hm={}
        count=0
        for i in range(len(nums)):
            if nums[i]-k in hm:
                count +=hm[nums[i]-k]
            if nums[i]+k in hm:
                count +=hm[nums[i]+k]
            if nums[i] in hm:
                hm[nums[i]] +=1
            else:
                hm[nums[i]] =1
        return count        