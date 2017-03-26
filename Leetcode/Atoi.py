def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    sign=1
    base=0
    i=0
    if str=='':
        return 0
    while(str[i]==' '):i+=1
    if(str[i]=='-'):
        sign=-1
    if(str[i]=='+'):
        sign=1
    while(i<len(str) and str[i]>='0' and str[i]<='9' ):
        if(base>214748364 or (base==214748364 and int(str[i])>7)):
            if(sign==1):
                return 2147483647
            if(sign==-1):
                return -2147483647
        base=10*base+int(str[i])
        i+=1
    return base*sign
