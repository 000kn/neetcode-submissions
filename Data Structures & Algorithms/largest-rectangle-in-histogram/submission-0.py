class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                hPop = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                height = heights[hPop]
                maxArea = max(maxArea, width * height)
            stack.append(i)

        while stack:
            hPop = stack.pop()
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            height = heights[hPop]
            maxArea = max(maxArea, width * height)
        return maxArea