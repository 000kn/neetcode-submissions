class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        numbers = {}

        for i in nums:
            numbers[i] = 1 + numbers.get(i, 0)

        return max(numbers, key=numbers.get)