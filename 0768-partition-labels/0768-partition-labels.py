class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i

        size = 0
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end, last[s[i]])
            if i == end:
                partitions.append(size)
                size = 0
        return partitions