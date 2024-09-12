class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumation=(n*(n+1))//2
        s2=sum(nums)
        missing=sumation - s2
        return missing
        