class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[', ')':'(', '}':'{'}
        stack = []
        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(bracket)
        return False if (stack) else True