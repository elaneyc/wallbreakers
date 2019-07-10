class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        target = list(p)
        target.sort()
        indices = []

        # Initial substring
        temp = list(s[0:len(p)])
        temp.sort()
        if temp == target:
            indices.append(0)

        for i in range(1, len(s)-len(p)+1):
            # Delete no longer relevant character
            remove = self.findRemoveIndex(temp, s[i - 1])
            if remove != None:
                del temp[remove]

            # Insert new character
            newC = s[i + len(p) - 1]
            addIdx = self.findInsertIndex(temp, newC)
            temp.insert(addIdx, newC)

            if temp == target:
                indices.append(i)

        return indices

    # Helper method to find the index of the character to remove
    def findRemoveIndex(self, s, c):
        if len(s) == 0:
            return None
        if s[0] == c:
            return 0
        elif s[-1] == c:
            return len(s)-1

        mid = len(s) / 2
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[mid] == c:
                return mid
            elif s[mid] > c:
                end = mid - 1
            elif s[mid] < c:
                start = mid + 1
            mid = (start + end) // 2

        # If not found
        return -1

    # Helper method to find where to insert new character
    def findInsertIndex(self, s, c):
        if len(s) == 0:
            return 0
        elif s[0] > c:
            return 0
        elif s[-1] < c:
            return len(s)

        mid = len(s) / 2
        start = 0
        end = len(s) - 1

        while start <= end:
            if c == s[mid] or (s[mid-1] < c and s[mid] > c):
                return mid
            elif c > s[mid]:
                start = mid + 1
            elif c < s[mid]:
                end = mid - 1
            mid = (start + end) // 2

                
