class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentmax = 0
        a, b = 0, len(heights) - 1
        while a<b:
            temp = min(heights[b],heights[a]) * (b-a)
            currentmax = max(currentmax,temp)
            if heights[a]<heights[b]:
                i = a
                while heights[i] <= heights[a] and i<b:
                    i += 1  
                a = i
            else:
                i = b
                while heights[i] <= heights[b] and a<i:
                    i = i-1
                b=i
        return currentmax
