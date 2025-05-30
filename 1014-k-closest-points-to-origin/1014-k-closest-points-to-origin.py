class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x, y = point[0], point[1]
            dist = x**2 + y**2
            return dist

        pointList = []
        heapq.heapify(pointList)
        for point in points:
            heapq.heappush(pointList, [-distance(point), point])
            if len(pointList) > k:
                heapq.heappop(pointList)

        ans = []
        while pointList:
            dist, point = heapq.heappop(pointList)
            ans.append(point)

        return ans