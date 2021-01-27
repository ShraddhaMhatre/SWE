<<<<<<< HEAD
#Amazon
#Jewels & Stones: You want to know how many of the stones you have are also jewels. e.g. Input: J = "aA", S = "aAAbbbb" Output: 3
class Solution(object):
    count = 0
    def numJewelsInStones(self, J, S):
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    self.count += 1
                else:
                    continue
        return self.count
       
=======
#Amazon
#Jewels & Stones: You want to know how many of the stones you have are also jewels. e.g. Input: J = "aA", S = "aAAbbbb" Output: 3
class Solution(object):
    count = 0
    def numJewelsInStones(self, J, S):
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    self.count += 1
                else:
                    continue
        return self.count
       
>>>>>>> a0b6eced5e477dd562f734cfdecd406240df9c6d
        