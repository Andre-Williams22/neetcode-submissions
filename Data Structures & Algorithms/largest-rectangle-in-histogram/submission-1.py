class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        stack = []
        max_area = 0 

        # traverse idx and values 
        for i, h in enumerate(heights):
            # while the curr bar is less than the bar at stack top 
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                # width is current idx minus idx of new stack top minus 1 
                if not stack: 
                    width = i 
                else:
                    width = (i - stack[-1]) - 1 
                max_area = max(max_area, height*width)
            stack.append(i)
        
        return max_area
