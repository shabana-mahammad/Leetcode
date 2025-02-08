class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        i=0
        j=len(nums)-1
        while i<j:
            sums=nums[i]+nums[j]
            if sums==k:
                count +=1
                i +=1
                j -=1
            elif sums<k:
                i +=1
            else:
                j -=1
        return count