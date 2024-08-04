class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxH = []
        
        for i in points:
            x = i[0]
            y = i[1]
            dist = x**2 + y**2
            maxH.append([dist, x, y])
        heapify(maxH)
        
        ans = []
        for _ in range(k):
            d, x, y = heappop(maxH)
            ans.append([x, y])
            
        return ans