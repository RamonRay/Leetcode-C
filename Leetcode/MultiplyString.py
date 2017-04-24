class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        out=[]
        l1=len(num1)
        l2=len(num2)
        for i in range(l1+l2):
            out.append('0')
        for index1,i in enumerate(num1[::-1]):
            carry=0
            for index2,j in enumerate(num2[::-1]):
                index=(index1+index2)
                tmp=int(out[index])+int(i)*int(j)+carry
                out[index]=str(tmp%10)
                carry=tmp/10
            out[index1+l2]=str(int(out[index1+l2])+carry)
        index=l1+l2-1
        while(index>0):
            if (out[index]!='0'):
                break
            index-=1
        ans=('').join(out[index::-1])
        return ans