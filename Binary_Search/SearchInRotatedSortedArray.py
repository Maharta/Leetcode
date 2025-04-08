class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # case 2 - array not rotated
        if nums[l] < nums[r]:
            while (l <= r):
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

        # case 1 - array rotated
        # left side of rotated sorted array
        # right side of rotated sorted array
        while (l <= r):
            m = (l + r) // 2

            if nums[m] == target:
                return m
            # we are at the left side of rotated array
            if nums[m] >= nums[-1]:
                if (target < nums[m] and target < nums[0]) or (target >= nums[m]):
                    l = m + 1
                elif target < nums[m] and target >= nums[0]:
                    r = m - 1
            elif nums[m] < nums[0]:
                if target < nums[m] or target > nums[-1]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
