<<<<<<< HEAD
class Solution(object):
    def isPowerOfThree(self, n):
      
        if (n == 0): 
            return False
        while (n != 1): 
            if (n % 3 != 0): 
                return False
            n = n // 3
              
        return True
=======
class Solution(object):
    def isPowerOfThree(self, n):
      
        if (n == 0): 
            return False
        while (n != 1): 
            if (n % 3 != 0): 
                return False
            n = n // 3
              
        return True
>>>>>>> a0b6eced5e477dd562f734cfdecd406240df9c6d
        