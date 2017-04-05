class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        lenstr = len(s)
        stack = [(-1, '')]
        ans = 0
        for i in range(lenstr):
            if s[i] == '(':
                stack.append((i, '('))
            else:
                if stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append((i, ')'))
        lenstack = len(stack)
        if lenstack == 1:
            return lens
        stack.append((lenstr, ''))
        for i in range(1, lenstack + 1):
            tmp = stack[i][0] - stack[i - 1][0] - 1
            if tmp > ans and tmp > 1:
                ans = tmp
        return ans

