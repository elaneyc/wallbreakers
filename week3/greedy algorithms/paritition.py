class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        chars = {}

        for i,c in enumerate(S):
            if c not in chars:
                chars[c] = {"beg": i, "end": i}
            else:
                chars[c]["end"] = i

        items = chars.items()
        items.sort()
        partitions = []
        start = 0
        end = 0
        for c, interval in items:
            if chars[c]["beg"] < start or (start <= chars[c]["beg"] and chars[c]["beg"] <= end):
                if chars[c]["end"] > end:
                    end = chars[c]["end"]
            else:
                partitions.append(end - start + 1)
                start = chars[c]["beg"]
                end = chars[c]["end"]

        partitions.append(end - start + 1)
        return partitions
        
