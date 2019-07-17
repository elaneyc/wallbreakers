class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1

        # reverse the first n-k elements
        self.reverse(nums, 0, end - k)

        # reverse the last k elements
        self.reverse(nums, end - k + 1, end)

        # reverse the entire array to rotate it
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
