class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        for bracket in s:
            if stack and bracket in pairs:
                if stack[-1] == pairs[bracket]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True
