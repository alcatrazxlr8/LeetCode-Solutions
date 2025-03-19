class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            tmp = sorted(s)
            tmp = "".join(tmp)
            if tmp not in dic:
                dic[tmp] = []
            dic[tmp].append(s)
        
        ans = []
        for key, value in dic.items():
            ans.append(value)

        return ans