class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        sums=0
        for i in range(len(nums)):
            sums +=nums[i]
            if sums > maxsum:
                maxsum=sums
            if sums<0:
                sums=0
        return maxsum
                