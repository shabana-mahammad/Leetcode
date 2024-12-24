class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr=[0]*101
        maxFreq=0
        for i in nums:
            arr[i] +=1
            maxFreq=max(maxFreq,arr[i])
        count=arr.count(maxFreq)
        return count*maxFreq