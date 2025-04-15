from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            maxCount = max(count.values())
            if (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l) + 1)
        return res

        # ABAAB K = 2
