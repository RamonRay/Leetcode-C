class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            if dividend>=0:
                return 2147483647
            else:
                return -2147483648
        if abs(dividend)<abs(divisor):
            return 0
        if ((dividend<0) ^ (divisor<0)):
            sign=-1
        else:
            sign=1
        l=abs(dividend)
        r=d=abs(divisor)
        k=0
        while (l>r):
            r<<=1
        while(r>=d):
            k<<=1
            if(l>=r):
                k+=1
                l-=r
            r>>=1
        if k<=2147483647:
            return sign*k
        else:
            if sign==1:
                return 2147483647
            else:
                return -2147483648