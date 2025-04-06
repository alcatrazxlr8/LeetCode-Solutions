from collections import deque
class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = collections.deque()
        self.s = set()
        self.d = defaultdict(list) # use this with key=dest

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        pkt = (source, destination, timestamp)
        # check if already exists
        if pkt in self.s:
            return False
        # check if exceeding memory limit
        if len(self.packets) == self.memoryLimit:
            # remove old packet from queue, set and dict
            old = self.packets.popleft()
            self.s.remove(old)
            self.d[old[1]].remove(old[2])
        # insert new packet into queue, set and dict
        self.packets.append(pkt)
        self.s.add(pkt)
        
        bisect.insort(self.d[destination], timestamp)
        return True

        # ##check if already exists
        # for pkt in self.packets:
        #     if pkt[0] == source and pkt[1] == destination and pkt[2] == timestamp:
        #         return False
        # ## check if len exceeding memoryLimit
        # numPackets = len(self.packets)
        # if numPackets == self.memoryLimit:
        #     self.packets.popleft()
        # self.packets.append([source, destination, timestamp])
        # return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        # return self.packets.popleft()
        pkt = self.packets.popleft()
        self.s.remove(pkt)
        self.d[pkt[1]].remove(pkt[2])
        return list(pkt)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time = self.d[destination]
        left = bisect.bisect_left(time, startTime)
        right = bisect.bisect_right(time, endTime)
        return right - left

        # count = 0
        # for pkt in self.packets:
        #     if pkt[1] == destination and endTime >= pkt[2] >= startTime:
        #         count += 1
        # return count


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)