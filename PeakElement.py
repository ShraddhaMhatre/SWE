#Yahoo
#Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
class Solution(object):
    result = 0
    def findPeakElement(self, nums):
        
        for i in range(len(nums)):
            
            if i == len(nums):
                #print i
                break
            try:    
                if nums[i] > nums[i+1]:
                    if nums[i] > nums[i-1]:
                        self.result = i
                        
                if nums[i+1] > nums[i]:
                    #print i
                    self.result = i+1
                    #print result
            except:
                #print i
                continue
        #print self.result
        return self.result
        """
        :type nums: List[int]
        :rtype: int
        """
        