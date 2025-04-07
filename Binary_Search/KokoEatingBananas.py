import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        minTime = 0

        while (l <= r):
            m = (l + r) // 2

            time = 0
            for pile in piles:
                eatPileTime = math.ceil(pile / m)
                time += eatPileTime

            if time > h:
                l = m + 1
            else:
                r = m - 1
                minTime = m

        return minTime
