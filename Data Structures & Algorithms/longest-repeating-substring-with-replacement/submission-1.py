class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])
            if (r - l + 1) - maxFreq <= k:
                res = max(maxFreq, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return res