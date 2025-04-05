class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        tuples = []

        for i in range(len(position)):
            tuples.append((position[i], speed[i]))

        posAndSpeed = sorted(tuples, key=lambda tuple: tuple[0])

        stack = []

        for i in range(len(posAndSpeed) - 1, -1, -1):

            if len(stack) == 0:
                stack.append(posAndSpeed[i])
                continue

            car = posAndSpeed[i]
            carInFront = stack[-1]

            carTime = (target - car[0]) / car[1]
            carInFrontTime = (target - carInFront[0]) / carInFront[1]

            if carTime > carInFrontTime:
                stack.append(posAndSpeed[i])

        return len(stack)
