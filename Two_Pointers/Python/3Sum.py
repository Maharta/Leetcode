class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            target = -nums[i]

            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif twoSum < target:
                    l += 1
                else:
                    r -= 1

        return out
