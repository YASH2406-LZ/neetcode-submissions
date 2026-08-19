class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if char == "+":
                    result = operand1 + operand2
                elif char == "-":
                    result = operand1 - operand2
                elif char == "*":
                    result = operand1 * operand2
                else:  # division
                    result = int(operand1 / operand2)  # truncate toward zero

                stack.append(result)

        return stack[0]