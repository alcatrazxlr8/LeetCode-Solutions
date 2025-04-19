class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        ans = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = "".join(sorted_s)
            ans[sorted_s].append(s)
        
        for key, value in ans.items():
            final.append(value)
        return final