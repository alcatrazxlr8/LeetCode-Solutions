class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        low = 1
        high = maxSpeed
        k = maxSpeed
        
        def canEat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        while low <= high:
            mid = low + (high-low)//2
            if canEat(mid):
                k = min(k, mid)
                high = mid - 1
            else:
                low = mid + 1

        return k