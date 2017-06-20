class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1
        if n<0:
            x=1.0/x
            n=-n
        m=1
        while m<=n:
            if n&m:
                ans*=x
            m<<=1
            x*=x
        return ans
            
