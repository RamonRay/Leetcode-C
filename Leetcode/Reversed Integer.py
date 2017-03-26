    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        k=1
        if x<0:
            k=-1
            x=-x
        while(x!=0):
            rev=rev*10+x%10
            x=x/10
            if(rev> 2147483647):
                return 0
        return rev*k
