from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Sort the characters by number of appearances
        s_count = Counter(s)
        s_count = s_count.items()
        s_count.sort(key = lambda c : c[1], reverse=True)

        # Create the sorted string
        answer = []
        for let, count in s_count:
            answer.append(let*count)

        return ''.join(answer)
