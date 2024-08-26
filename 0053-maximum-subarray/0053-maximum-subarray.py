class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currsum=nums[0]
        for i in range(1,len(nums)):
            currsum=max(nums[i],nums[i]+currsum)
            maxsum=max(maxsum,currsum)
        return maxsum
        