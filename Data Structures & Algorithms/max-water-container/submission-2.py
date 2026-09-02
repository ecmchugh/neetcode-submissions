class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        container = 0

        while l < r:
            res = (r-l) * min(heights[l], heights[r])
            container = max(container, res)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return container

        
        
