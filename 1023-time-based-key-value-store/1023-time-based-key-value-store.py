class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        
        # find max value <= x
        def binary_search(arr, target_timestamp):
            low, high = 0, len(arr) - 1
            res = -1  # default to "not found"
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] <= target_timestamp:
                    res = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        i = binary_search(arr, timestamp)

        return arr[i][1] if i != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)