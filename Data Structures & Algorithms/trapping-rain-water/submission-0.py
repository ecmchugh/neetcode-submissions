class Solution:
    def trap(self, height: List[int]) -> int:
        maxRight = [0] * len(height)
        maxLeft = [0] * len(height)
        for i in range(len(height)):
            if i == 0: 
                maxL = height[i]
            else:
                maxLeft[i] = maxL
                maxL = max(maxL, height[i])
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                maxR = height[i]
            else:
                maxRight[i] = maxR
                maxR = max(maxR, height[i])
        total = 0
        for i in range(len(height)):
            minWater = min(maxRight[i], maxLeft[i])
            if minWater - height[i] > 0:
                total += (minWater-height[i])
        return total