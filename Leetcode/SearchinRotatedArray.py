class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return -1
        low=0
        high=len(nums)-1
        while(low<high):
            mid=(low+high)/2
            if(nums[0]>target)^(nums[0]>nums[mid])^(target>nums[mid]):
                low=mid+1
            else:
                high=mid
        if low==high and nums[low]==target:
            return low
        else:
            return -1