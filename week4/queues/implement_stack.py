class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []
        self.back = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.front.append(x)
        self.back.insert(0, self.front.pop())


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return -1
        else:
            return self.back.pop(0)



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return -1
        else:
            return self.back[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.back) == 0




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
