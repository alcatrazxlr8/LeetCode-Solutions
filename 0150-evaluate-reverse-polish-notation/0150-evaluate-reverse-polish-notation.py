class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operators = {"+", "-", "*", "/"}
        op = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "*": lambda x, y: x * y,
              "/": lambda x, y: int(x / y)}
        
        stack = []
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:    
                op2 = stack.pop()
                op1 = stack.pop()
                newOp = op[i](op1, op2)
                print(newOp)
                stack.append(newOp)
                
        return stack[0]
            
            
                