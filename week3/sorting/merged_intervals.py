class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals

        intervals.sort()

        merged = [intervals[0]]

        current = 0
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] <= end:
                if i[1] > merged[current][1]:
                    merged[current][1] = i[1]
                    end = i[1]
            else:
                current += 1
                merged.append(i)
                start = i[0]
                end = i[1]

        return merged
