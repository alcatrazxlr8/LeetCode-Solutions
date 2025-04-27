class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+":operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for t in tokens:
            if stack and t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                op = ops.get(t)
                ans = int(op(op1, op2))
                print(f"{op1} {op} {op2} = {ans}")
                stack.append(ans)

            else:
                stack.append(int(t))

        return stack[0]
        