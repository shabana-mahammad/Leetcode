class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        st=set()
        i=0
        j=0
        while j<n:
            if abs(i-j) > k:
                st.remove(nums[i])
                i +=1
            if nums[j] in st:
                return True
            st.add(nums[j])
            j +=1 
        return False