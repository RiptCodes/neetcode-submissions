class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "/", "*"}
        for token in tokens:
            if token in operands:
                # do calculations
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(token))


            
        return stack[0]

        