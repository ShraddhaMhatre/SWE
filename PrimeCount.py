#Yahoo
#Count the number of prime numbers less than a non-negative number, n. E.g.I/P=10; O/P=4 (2,3,5,7)
class Solution(object):
    numList = [2]
    def countPrimes(self, n):
        count = 0
        primeCount = 0
        for j in range(2,n):
            primeCount = self.isPrime(j)
            if primeCount:
                count += 1
        return count
    
    #True:1 False:0
    def isPrime(self,num):
        if num in self.numList:
            return 1
        if num > 1:
            for k in self.numList:  
                if num % k == 0:
                    return 0  
        self.numList.append(num)
        return 1      