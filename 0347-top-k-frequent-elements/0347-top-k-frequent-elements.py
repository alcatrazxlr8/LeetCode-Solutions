class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(count)
        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
        # print(sorted_count)
        ans = []
        for i in range(k):
            ans.append(sorted_count[i][0])
        return ans