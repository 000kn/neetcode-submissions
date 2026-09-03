class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixDict = { 0 : 1 }

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixDict.get(diff, 0)
            prefixDict[curSum] = 1 + prefixDict.get(curSum, 0)
        return res
