class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target[0], target[1], target[2]
        maxA, maxB, maxC = 0, 0, 0
        for i in range(len(triplets)):
            if (a < triplets[i][0] or b < triplets[i][1] or c < triplets[i][2]) or (a != triplets[i][0] and b != triplets[i][1] and c != triplets[i][2]):
                continue
            else:
                maxA, maxB, maxC = max(maxA, triplets[i][0]), max(maxB, triplets[i][1]), max(maxC, triplets[i][2])

        return True if (maxA, maxB, maxC) == (a, b, c) else False
                

