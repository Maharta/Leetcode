class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        out = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if i == len(temperatures) - 1:
                stack.append((temperatures[i], i))
                out[i] = 0
                continue

            while (top := stack.pop()) if stack else False:
                if temperatures[i] < top[0]:
                    stack.append(top)
                    stack.append((temperatures[i], i))
                    out[i] = top[1] - i
                    break

            if len(stack) == 0:
                stack.append((temperatures[i], i))
                out[i] = 0
        return out
