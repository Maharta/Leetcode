class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]

        res = 5000

        while l <= r:
            m = (l + r) // 2
            # left sorted array
            res = min(res, nums[m])
            if nums[m] >= nums[l] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res
                
