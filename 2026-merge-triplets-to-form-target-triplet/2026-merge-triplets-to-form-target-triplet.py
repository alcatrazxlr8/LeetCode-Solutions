class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target[0], target[1], target[2]
        maxA, maxB, maxC = 0, 0, 0
        for i in range(len(triplets)):
            # we cant go over target values(1st condition) & we dont need triplets that have none of the target values (2nd condition)
            if (triplets[i][0] > a or triplets[i][1] > b or triplets[i][2] > c) or (a != triplets[i][0] and b != triplets[i][1] and c != triplets[i][2]):
                continue
            else:
                maxA, maxB, maxC = max(maxA, triplets[i][0]), max(maxB, triplets[i][1]), max(maxC, triplets[i][2])

        return (maxA, maxB, maxC) == (a, b, c)
        # return True if (maxA, maxB, maxC) == (a, b, c) else False
                

