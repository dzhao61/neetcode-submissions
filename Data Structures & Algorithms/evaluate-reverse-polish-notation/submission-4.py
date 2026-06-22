class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+" and len(stack)>1:
                k = stack.pop()
                l = stack.pop()
                stack.append(int(k+l))
            elif i == "-" and len(stack)>1:
                k = stack.pop()
                l = stack.pop()
                stack.append(int(l-k))
            elif i == "*" and len(stack)>1:
                k = stack.pop()
                l = stack.pop()
                stack.append(int(k*l))
            elif i == "/" and len(stack)>1:
                k = stack.pop()
                l = stack.pop()
                stack.append(int(l/k))
            else:
                stack.append(int(i))
            print(stack)
        
        return stack.pop()
        