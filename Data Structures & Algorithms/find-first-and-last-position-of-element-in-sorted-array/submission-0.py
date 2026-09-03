class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left side
        l, r = 0, len(nums) - 1
        first = -1
        while l <= r:
            mid = (l+r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                first = mid
                r = mid - 1
        
        # right side
        l, r = 0, len(nums) - 1
        last = -1
        while l <= r:
            mid = (l+r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                last = mid
                l = mid + 1
        return [first, last]