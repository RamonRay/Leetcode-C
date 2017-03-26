def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m=len(s)
    n=len(p)
    dp=[[] for i in range (m+1)]
    for i in range(m+1):
        for j in range(n+1):
            dp[i].append(False)
    dp[0][0]=True
    for i in range(m+1):
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[i][j]=dp[i][j-2] or (i>0 and (s[i-1]==p[j-2] or p[j-2]=='.') and dp[i-1][j])
            else:
                dp[i][j]= i>0 and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
    for i in range(1,n+1):
        print dp[0][i]
    return dp[m][n]
