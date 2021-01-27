<<<<<<< HEAD
#Rotate array nums by k
class Solution:
    
    def rotate(self, nums, k):
        n = len(nums) - k
=======
#Rotate array nums by k
class Solution:
    
    def rotate(self, nums, k):
        n = len(nums) - k
>>>>>>> a0b6eced5e477dd562f734cfdecd406240df9c6d
        nums[:] = nums[n-k:] + nums[:n-k]