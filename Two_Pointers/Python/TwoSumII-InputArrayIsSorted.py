class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while (l < r):
            res = numbers[r] - numbers[l]
            if res == target:
                return [l + 1, r]
            if res < target:
                l += 1
            else:
                r -= 1
        return []

        
         