class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<nums[(mid-1+n)%n] and nums[mid]<nums[(mid+1)%n]:
                return nums[mid]
            elif nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        return nums[0]