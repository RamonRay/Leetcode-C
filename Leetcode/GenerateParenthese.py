class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=[]
        def generate(tmp,left,right):
            if left: generate(tmp+'(',left-1,right)
            if left<right: generate(tmp+')',left,right-1)
            if not right:
                s.append(tmp)
                return
        generate('',n,n)
        return s
