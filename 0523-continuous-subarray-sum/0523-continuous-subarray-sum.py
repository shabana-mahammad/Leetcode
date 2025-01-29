class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm={0:-1}
        sums=0
        for i in range(len(nums)):
            sums +=nums[i]
            reminder = sums % k
            if reminder in hm:
                if i-hm[reminder] >= 2:
                    return True
            else:
                hm[reminder] = i
        return False