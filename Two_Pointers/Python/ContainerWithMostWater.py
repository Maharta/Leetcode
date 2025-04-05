class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1

        mostWater = 0

        while l < r:
            waterHeight = min(height[l], height[r])
            mostWater = max(mostWater, waterHeight * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mostWater
