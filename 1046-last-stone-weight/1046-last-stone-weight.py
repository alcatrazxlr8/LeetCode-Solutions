class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = (-1) * stones
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        # print(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)

            if max2 > max1:
                heapq.heappush(stones, max1-max2)

        stones.append(0)
        return abs(stones[0])