class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        # memoriaziation thing
        dp = [0] * len(nums)

        # base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # after 3. index then we decide

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]