class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=[]
        for i in s:
            if i =='(':
                x.append(')')
            elif i=='[':
                x.append(']')
            elif i=='{':
                x.append('}')
            else:
                if x==[] or i!=x.pop():
                    return False
        return x==[]
                
