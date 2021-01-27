<<<<<<< HEAD
class Solution(object):
    def isPowerOfTwo(self, n):
        if (n == 0): 
            return False
        while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
        return True
=======
class Solution(object):
    def isPowerOfTwo(self, n):
        if (n == 0): 
            return False
        while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
        return True
>>>>>>> a0b6eced5e477dd562f734cfdecd406240df9c6d
        