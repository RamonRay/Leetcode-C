class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums==[]:
            return []
        def findNnums(nums,target,N,result,results):
            if len(nums)<N or N<2 or N*nums[0]>target or N*nums[-1]<target:
                return
            if N==2:
                l,r=0,len(nums)-1
                while(l<r):
                    out=nums[l]+nums[r]
                    if out==target:
                        results.append(result+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while(l<r and nums[r]==nums[r+1]):
                            r-=1
                    elif out<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(len(nums)-N+1):
                    if i==0 or nums[i-1]!=nums[i]:
                        findNnums(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
        results=[]
        findNnums(sorted(nums),target,4,[],results)
        return results
