class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.hashset:
            self.hashset.append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashset:
            self.hashset.remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
