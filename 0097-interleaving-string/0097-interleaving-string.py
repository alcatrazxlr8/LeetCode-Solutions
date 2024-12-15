class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def rec(i, j, k):
            if k == len(s3):
                return True
            if (i,j,k) in dp:
                return dp[(i,j,k)]

            choice1, choice2 = False, False

            if i < len(s1) and s3[k] == s1[i]:
                choice1 = rec(i+1, j, k+1)
            if j < len(s2) and s3[k] == s2[j]:
                choice2 = rec(i, j+1, k+1)
            
            res = choice1 or choice2
            dp[(i,j,k)] = res

            return res

        return rec(0,0,0)

            # if i >= len(s1) or j >= len(s2):
            #     return False
        #     if (i < len(s1) and j < len(s2)) and s3[k] != s1[i] and s3[k] != s2[j]:
        #         print(f"case1 - False - {i},{j},{k}")
        #         return False
        #     elif s3[k] == s1[i] and s3[k] != s2[j]:
        #         print(f"case2 - {i+1},{j},{k+1}")
        #         return rec(i+1, j, k+1)
        #     elif s3[k] != s1[i] and s3[k] == s2[j]:
        #         print(f"case3 - {i},{j+1},{k+1}")
        #         return rec(i, j+1, k+1)
            
        #     print(f"case4 - i - {i+1},{j},{k+1}")
        #     print(f"case4 - j - {i},{j+1},{k+1}")
        #     return rec(i+1, j, k+1) or rec(i, j+1, k+1)

        #     # print(f"{iteration}")
        #     # return True
        # return rec(0,0,0)