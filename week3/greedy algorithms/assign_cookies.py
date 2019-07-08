class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        num_children = len(g)
        content = 0
        child = 0
        for cookie in s:
            if content >= num_children:
                break
            # Only increase child if found a content one
            if cookie >= g[child]:
                content += 1
                child += 1

        return content
                
