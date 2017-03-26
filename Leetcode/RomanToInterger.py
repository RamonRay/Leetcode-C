class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        sum=0
        sum+=s.count('M')*1000
        sum+=s.count('D')*500
        sum+=s.count('C')*100
        sum+=s.count('L')*50
        sum+=s.count('X')*10
        sum+=s.count('V')*5
        sum+=s.count('I')
        if 'IV' in s:
            sum-=2
        if 'IX' in s:
            sum-=2
        if 'XL' in s:
            sum-=20
        if 'XC' in s:
            sum-=20
        if 'CD' in s:
            sum-=200
        if 'CM' in s:
            sum-=200
        return sum
