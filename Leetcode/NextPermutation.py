class Solution(object):
    def nextPermutation(self, nums):
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