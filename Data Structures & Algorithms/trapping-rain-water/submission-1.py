class Solution:
    def trap(self, height: List[int]) -> int:
        maxRight = [0] * len(height)
        maxLeft = [0] * len(height)
        maxL = height[0]
        maxR = height[len(height)-1]
        for i in range(1, len(height)):
            maxLeft[i] = maxL
            maxL = max(maxL, height[i])
        for i in range(len(height)-2,-1,-1):
            maxRight[i] = maxR
            maxR = max(maxR, height[i])
        total = 0
        for i in range(len(height)):
            minWater = min(maxRight[i], maxLeft[i])
            if minWater - height[i] > 0:
                total += (minWater-height[i])
        return total