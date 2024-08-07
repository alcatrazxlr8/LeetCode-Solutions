class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)
        
        time = 0
        q = deque() ## pairs of [-cnt, idleTime]
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heappop(maxHeap) ## since maxheap is -cnt values, we add to reduce them
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
                
        return time
                
                