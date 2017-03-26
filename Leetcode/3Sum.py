class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=qsort(self,nums)
        ans=[]
        i=0
        while(i<len(nums)):
            target=-nums[i]
            front=i+1
            back=len(nums)-1
            while(front<back):
                sum=nums[front]+nums[back]
                if(sum<target):
                    front+=1
                elif(sum>target):
                    back-=1
                else:
                    tri=[]
                    tri.append(nums[i])
                    tri.append(nums[front])
                    tri.append(nums[back])
                    ans.append(tri)
                    while(front<back and nums[front]==tri[1]):
                        front+=1
                    while(front<back and nums[back]==tri[2]):
                        back-=1
            while(i+1<len(nums) and nums[i+1]==nums[i]):
                i+=1
            i+=1
        return ans
    def qsort(self,L):
        if len(L) <= 1:
            return L
        return qsort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + qsort([ge for ge in L[1:] if ge >= L[0]])
                    
