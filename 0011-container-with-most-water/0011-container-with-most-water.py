class Solution(object):
    def maxArea(self, height):
        start_point, end_point = 0, len(height) - 1
        max_area = 0
        while start_point < end_point:
            min_height = (end_point-start_point) * min(height[start_point], height[end_point])
            max_area = max(max_area, min_height)
            if height[start_point] < height[end_point]:
                start_point += 1
            else:
                end_point -= 1
        return max_area