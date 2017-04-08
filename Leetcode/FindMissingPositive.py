class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        nums.append(0)
        lennums=len(nums)
        while(i<len(nums)):
            if i+1==nums[i]:
                i+=1
                continue
            while (nums[i] >= 1 and nums[i] <= lennums and nums[nums[i]-1]!=nums[i]):
                tmp = nums[i]
                nums[i]=nums[tmp-1]
                nums[tmp-1]=tmp
            i+=1
        for i in range(lennums):
            if i+1!=nums[i]:
                return i+1
        return lennums+1