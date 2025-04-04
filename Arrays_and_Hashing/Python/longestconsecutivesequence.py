class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numberSet = set(nums)
        maxSeq = 0

        for num in numberSet:
            if (num - 1) in numberSet:
                continue
            seq = 1

            x = num + 1
            while x in numberSet:
                seq += 1
                x = x + 1
            
            maxSeq = max(maxSeq, seq)
        return maxSeq



        
            