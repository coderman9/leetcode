class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        cur_max = float("-inf")
        for i in range(len(points) - 1):
            dist = points[i + 1][0] - points[i][0]
            if  dist > cur_max:
                cur_max = dist
        return cur_max
