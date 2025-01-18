class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # I think we first find the rough place the newInterval should fit in according to its start (since we want sorted starts).
        # Then we see if it overlaps or not
        # if it doesnt overlap, we insert it and return
        # if it does overlap, we see with which pre exiositng intervals it overlaps
            # to find overlap, we basically find the min(start) and max(end)
        if not intervals:
            return [newInterval]
        #binary search
        n = len(intervals)
        left = 0
        right = n
        while left < right:
            mid = left + (right-left) // 2
            if newInterval[0] < intervals[mid][0]:
                right = mid
            else:
                left = mid + 1

        intervals.insert(left, newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res