class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for c in tokens:
            if c in "+-*/":
                num1 = self.stack.pop()
                num2 = self.stack.pop()

                if c == "+":
                    self.stack.append(num2 + num1)
                elif c == "-":
                    self.stack.append(num2 - num1)
                elif c == "*":
                    self.stack.append(num2 * num1)
                elif c == "/":
                    self.stack.append(int(num2 / num1))
            else:
                self.stack.append(int(c))

        return self.stack[0]