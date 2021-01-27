#Rotate array nums by k
class Solution:
    
    def rotate(self, nums, k):
        n = len(nums) - k
        nums[:] = nums[n-k:] + nums[:n-k]