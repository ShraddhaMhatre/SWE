<<<<<<< HEAD
class Solution(object):
    def isPowerOfFour(self, num):
        if (num == 0): 
            return False
        while (num != 1): 
            if (num % 4 != 0): 
                return False
            num = num // 4
              
=======
class Solution(object):
    def isPowerOfFour(self, num):
        if (num == 0): 
            return False
        while (num != 1): 
            if (num % 4 != 0): 
                return False
            num = num // 4
              
>>>>>>> a0b6eced5e477dd562f734cfdecd406240df9c6d
        return True