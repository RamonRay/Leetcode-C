class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==[]:
            return 0
        l=0
        for i in nums:
            if i!=val:
                nums[l]=i
                l+=1
        return l