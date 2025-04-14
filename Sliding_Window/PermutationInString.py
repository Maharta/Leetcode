from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        length = len(s1)
        s1count = defaultdict(int)
        count = defaultdict(int)

        for i in range(len(s1)):
            s1count[s1[i]] += 1

        for r in range(len(s2)):
            count[s2[r]] += 1

            if (r - l + 1) > length:
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1

            if ((r - l) + 1) == length and count == s1count:
                return True

        return False
