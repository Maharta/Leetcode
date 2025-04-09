# Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest without duplicate characters.

# Example 1:
# Input: s = "abcaxbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        longest = 0

        windowSet = set()

        while (r < len(s)):
            while s[r] in windowSet:
                windowSet.remove(s[l])
                l += 1
            windowSet.add(s[r])
            longest = max(r - l, longest)

        return longest


Solution().lengthOfLongestSubstring("abcabcbb")
