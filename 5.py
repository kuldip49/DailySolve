class Solution:
    def findmypow(self,x,n):
        if n == 0:
            return 1
        a = self.findmypow(x,n//2)
        if n % 2 == 0:
            return a*a
        else:
            return a * a * x
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.findmypow(x,n)
        else:
            return 1/self.findmypow(x,n*(-1))