class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        stack=[]
        res={}
        for j in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[j]:
                stack.pop()
            res[nums2[j]]=stack[-1] if stack else -1
            stack.append(nums2[j])
        return [res[i] for i in nums1]

