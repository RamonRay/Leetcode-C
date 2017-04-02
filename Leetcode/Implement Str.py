class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        lenh=len(haystack)
        lenn=len(needle)
        if lenh<lenn:
            return -1
        i=0
        while i < (lenh-lenn+1):
            if haystack[i:i+lenn]==needle:
                return i
            i+=1
        return -1