class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def numHours(k: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours

        maxPile = max(piles)
        low = 1
        high = maxPile
        minK = high

        while low <= high:
            k = low + (high-low)//2
            hours = numHours(k)
            # print(f"low: {low}; high: {high}; k: {k}; hours: {hours}")
            if hours <= h:
                minK = min(minK, k)
                high = k - 1
            else:
                low = k + 1
            # print(f"low: {low}; high: {high}; k: {k}; hours:{hours}; minK: {minK}")
        return minK