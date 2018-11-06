#Amazon
#Given an array, rotate the array to the right by k steps, where k is non-negative
from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        try:
            content = deque(nums)
            content.rotate(k)
            nums[:] = content
        except IndexError:
            pass
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """