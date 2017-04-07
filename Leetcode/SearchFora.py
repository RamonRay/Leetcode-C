class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1,-1]
        left=0
        right=len(nums)-1
        while(left<right):
            mid=(left+right)/2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if nums[left]==target:
            leftans=left
        else:
            return [-1,-1]
        left=0
        right=len(nums)-1
        while(left<right):
            mid=(left+right+1)/2
            if nums[mid]>target:
                right=mid-1
            else:
                left=mid
        rightans=left
        return [leftans,rightans]