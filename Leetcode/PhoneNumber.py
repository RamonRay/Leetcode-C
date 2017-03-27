class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result=['']
        for i in range(len(digits)):
            if not('0'<=digits[i]<='9'):
                break
            candidate=kvmaps[digits[i]]
            if candidate==None:
                continue
            for k in range(len(result)):
                tmp=result.pop()
                for j in range(len(candidate)):
                    result.insert(0,tmp+candidate[j])
        result.reverse()
        return result
