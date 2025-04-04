class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = set(['+', '-', '*', '/'])

        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = Solution.evaluate(token, operand1, operand2)
                stack.append(res)
        return stack.pop()

    @staticmethod
    def evaluate(operator, operand1, operand2):
        operand1 = int(operand1)
        operand2 = int(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '/':
            return int(operand1 / operand2)
        else:
            return operand1 * operand2


# x = Solution().evalRPN(["10", "6", "9", "3", "+",
#                         "-11", "*", "/", "*", "17", "+", "5", "+"])


# ["4","13","5","/","+"]
