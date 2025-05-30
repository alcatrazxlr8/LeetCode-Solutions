class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x, y = point[0], point[1]
            dist = x**2 + y**2
            return dist
        pointList = []
        for point in points:
            pointList.append([distance(point), point[0], point[1]])

        ans = []
        heapq.heapify(pointList)
        for _ in range(k):
            dist, x, y = heapq.heappop(pointList)
            ans.append([x, y])

        return ans