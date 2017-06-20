
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans={}
        x=ord('a')
        prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        for word in strs:
            key=1
            for letter in word:
                key*=prime[ord(letter)-x]
            if key in ans:
                ans[key].append(word)
            else:
                ans[key]=[word]
        new_ans=[ans[i] for i in ans]
        return new_ans
        
            
            
