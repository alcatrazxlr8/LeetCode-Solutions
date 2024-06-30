class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        # if len(s) % 2 != 0:
        #     return False
        for i in s:
            if i in dic:
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return True if not stack else False