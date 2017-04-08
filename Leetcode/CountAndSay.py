class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def answer(n):
            if n == 1:
                return '1'
            if n == 2:
                return '11'
            else:
                s = answer(n - 1)
                news = ''
                k = 1
                for i in range(1, len(s) + 1):
                    if not (i == len(s)) and s[i] == s[i - 1]:
                        k += 1
                    else:
                        news = news + str(k) + s[i - 1]
                        k = 1
                return news

        return answer(n)