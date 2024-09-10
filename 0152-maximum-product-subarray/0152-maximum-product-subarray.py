class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        maxi=ans
        mini=ans
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxi,mini=mini,maxi
            maxi=max(nums[i],maxi*nums[i])
            mini=min(nums[i],mini*nums[i])
            ans=max(ans,maxi)
        return ans