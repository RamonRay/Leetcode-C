class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=''
        i=0
        while(len(strs)>0):
            for j in range(len(strs)):
                if(i>=len(strs[j])) or (j>0 and strs[j][i]!=strs[j-1][i]):
                    return prefix
            prefix+=strs[0][i]
            i+=1
        return prefix
        
        
