class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        n=len(nums)
        maj=nums[0]
        current=1
        for i in range(1,n):
            if current==0:
                current +=1
                maj=nums[i]
            elif maj==nums[i]:
                current +=1
            else:
                current -=1
        return maj         