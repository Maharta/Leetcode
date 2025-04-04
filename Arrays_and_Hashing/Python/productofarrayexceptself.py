class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = [1] * len(nums)
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            out[i] = postfix * out[i]
            postfix *= nums[i]
    
        return out