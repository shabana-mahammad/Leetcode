class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hm={}
        for i in range(n):
            req=target-nums[i]
            if nums[i] in hm:
                return [hm[nums[i]],i]
            hm[req]=i
        return []