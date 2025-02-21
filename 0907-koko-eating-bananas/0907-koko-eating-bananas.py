class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        def eatAll(speed):
            hours=0
            for i in piles:
                hours +=(i+speed-1)//speed
            return hours<=h
        while l<r:
            mid=(l+r)//2
            if eatAll(mid):
                r=mid
            else:
                l=mid+1
        return l