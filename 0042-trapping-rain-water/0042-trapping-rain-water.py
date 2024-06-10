class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            # minMax = min(maxLeft, maxRight)
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(height[left], maxLeft)
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                water += maxRight - height[right]

        return water

        # ##### Difference in order of statements in outer if resulted in needing to explicitly check for negative water
        # while left < right:
        #     minMax = min(maxLeft, maxRight)
        #     if maxLeft <= maxRight:
        #         left += 1
        #         currWater = minMax - height[left]
        #         if currWater < 0:
        #             currWater = 0
        #         water += currWater
        #         if height[left] > maxLeft:
        #             maxLeft = height[left]
        #     else:
        #         right -= 1
        #         currWater = minMax - height[right]
        #         if currWater < 0:
        #             currWater = 0
        #         water += currWater
        #         if height[right] > maxRight:
        #             maxRight = height[right]
        # return water