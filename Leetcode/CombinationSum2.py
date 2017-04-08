class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans=[]
        lenc=len(candidates)
        def findAnswer(target,result,start):
            if target==0:
                ans.append(result)
                return             
            if target<0 or start==lenc:
                return
            i=start
            while(i<lenc):
                findAnswer(target-candidates[i],result+[candidates[i]],i+1)
                while(i<lenc-1 and candidates[i]==candidates[i+1]):
                    i+=1
                i+=1
        findAnswer(target,[],0)
        return ans