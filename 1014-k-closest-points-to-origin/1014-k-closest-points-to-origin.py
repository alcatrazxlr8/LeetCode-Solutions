class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = x**2 + y**2
            maxH.append([dist, x, y])
        heapify(maxH)
        ans = []
        for _ in range(k):
            dist, x, y  = heappop(maxH)
            ans.append([x, y])
        return ans