class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        points.sort()

        start = points[0][0]
        end = points[0][1]
        overlaps = 0
        for i in range(1, len(points)):
            # If end is greater than beginning or end coords, then overlaps
            if points[i][1] <= end:
                overlaps += 1
                end = points[i][1]
            elif points[i][0] <= end:
                overlaps += 1
                start = points[i][0]
            else:
                start = points[i][0]
                end = points[i][1]

        return len(points) - overlaps
