class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                min_h = min(heights[i], heights[j])
                area = min_h * (j-i)
                best_area = max(best_area, area)
        return best_area

        