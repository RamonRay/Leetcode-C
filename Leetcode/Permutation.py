class Solution(object):
    def nextpermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=i=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        j=i
        while j<k:
            nums[j],nums[k]=nums[k],nums[j]
            j+=1
            k-=1
        if i>0:
            k=i=i-1
            while(nums[k]<=nums[i]):
                k+=1
            nums[k],nums[i]=nums[i],nums[k]
        return nums
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        ans=[]
        ans.append(nums)
        middle=[i for i in nums]
        while True:
            middle=self.nextpermutation(middle)
            if middle==nums:
                break
            tmp=[i for i in middle]
            ans.append(tmp)
        return ans
