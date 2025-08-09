class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"*": operator.mul, "/": operator.truediv, "+": operator.add, "-": operator.sub}

        stack = []
        for token in tokens:
            # while stack:
            if token in operations and stack:
                ## we pop 2 elements
                y = stack.pop()
                x = stack.pop()
                ## compute the result
                res = operations[token](x, y)
                ## push result back in
                stack.append(int(res))

            else:
                stack.append(int(token))
        return int(stack[0])