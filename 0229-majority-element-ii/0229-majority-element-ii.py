class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] +=1 
            else:
                hm[nums[i]] =1
        result=[]
        for num in hm:
            if hm[num]>len(nums)/3:
                result.append(num)
        return result
        