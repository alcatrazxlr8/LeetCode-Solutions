class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            return point[0]**2 + point[1]**2
        
        dist_heap = [(-distance(point), point) for point in points]
        heapq.heapify(dist_heap)
        print(dist_heap)

        while len(dist_heap) > k:
            heapq.heappop(dist_heap)

        return [point[1] for point in dist_heap]