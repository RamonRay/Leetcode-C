class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if candidates == []:
            return []
        ans = []
        lenc = len(candidates)

        def findAnswer(target, result, biggest):
            if target == 0:
                ans.append(result)
            if target < 0:
                return
            for i in range(biggest, lenc):
                findAnswer(target - candidates[i], result + [candidates[i]], i)

        findAnswer(target, [], 0)
        return ans
