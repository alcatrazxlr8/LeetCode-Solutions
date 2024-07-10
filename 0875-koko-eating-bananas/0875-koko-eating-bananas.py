class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binSearchList = []
        # for i in range(minPiles, maxPiles):
        #     binSearchList.append(i)
        
        left = 1
        right = max(piles)
        minK = right
        
        while(left <= right):
            k = left + int((right - left)/2)
            # print("K:", k)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                # print(hours)
            # if hours == h:
            #     minK = min(k, minK)
            if hours <= h:
                minK = min(k, minK)
                right = k - 1
            else:
                left = k + 1
            
        return minK