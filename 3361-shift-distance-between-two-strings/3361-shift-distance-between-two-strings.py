class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        
        totalCost = 0
        for i in range(len(s)):
            start = ord(s[i]) - ord('a') 
            end = ord(t[i]) - ord('a')
            
            if start == end:
                continue
                
            fwd = (end - start + 26) % 26
            fwdCost = 0
            for j in range(fwd):
                fwdCost += nextCost[(start + j) % 26]
            
            bwd = (start - end + 26) % 26
            bwdCost = 0
            for j in range(bwd):
                bwdCost += previousCost[(start - j) % 26]
                
            totalCost += min(fwdCost, bwdCost)
            
        return totalCost