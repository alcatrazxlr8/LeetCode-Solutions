class Router:

    def __init__(self, memoryLimit: int):
        self.memory = 0
        self.memoryLimit = memoryLimit
        self.router = deque()
        self.dupe = set()
        self.d = defaultdict(list) # {dest: [timestamp1, timestamp2], .........}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        ## first check for duplicates
        packet = [source, destination, timestamp]
        if tuple(packet) in self.dupe:
            return False
        ## then check memory
        if self.memory == self.memoryLimit:
            removed = self.router.popleft()
            self.dupe.remove(tuple(removed))
            self.d[removed[1]].remove(removed[2])
            self.memory -= 1

        self.router.append(packet)
        self.dupe.add(tuple(packet))
        bisect.insort(self.d[destination], timestamp)
        self.memory += 1
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.router):
            packet = self.router.popleft()
            self.dupe.remove(tuple(packet))
            self.d[packet[1]].remove(packet[2])
            self.memory -= 1
            return packet
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time = self.d[destination]
        left = bisect.bisect_left(time, startTime)
        right = bisect.bisect_right(time, endTime)
        return (right - left)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)