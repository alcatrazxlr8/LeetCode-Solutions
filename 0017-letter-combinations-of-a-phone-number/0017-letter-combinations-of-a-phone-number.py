class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ## 
        numLetterMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        n = len(digits)
        ans = []
        
        def rec(i, tmp):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for c in numLetterMap[digits[i]]:
                rec(i+1, tmp + c)
                
        if digits:
            rec(0, "")
        return ans