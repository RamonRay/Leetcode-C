def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s==' ':
        return ' '
    if len(s)==1: 
        return s
    min_start=0
    max_len=1
    print len(s)
    i=0
    while(i<len(s)):
        if(len(s)-i<max_len/2):
            break
        j=i
        k=i
        while(k<len(s)-1 and s[k+1]==s[k]):
            k+=1
        i=k+1
        while(k<len(s)-1 and j>0 and s[k+1]==s[j-1]):
            k+=1
            j-=1
        new_len=k-j+1
        if(new_len>max_len):
                min_start=j
                max_len=new_len
    r=s[min_start:min_start+max_len]
    print min_start
    print max_len
    return r
       
