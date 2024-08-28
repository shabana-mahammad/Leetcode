class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posindex=0
        neindex=1 
        ans=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                ans[posindex]=nums[i]
                posindex +=2 
            else:
                ans[neindex]=nums[i]
                neindex +=2 
        return ans