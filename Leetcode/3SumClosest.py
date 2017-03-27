class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans=nums[0]+nums[1]+nums[len(nums)-1]
        i=0
        while i<len(nums)-2:
            left=i+1
            right=len(nums)-1
            while(left<right):
                out=nums[i]+nums[left]+nums[right]
                if(out<target):
                    left+=1
                elif(out>target):
                    right-=1
                else:
                    return target
                if(abs(out-target)<abs(ans-target)):
                    ans=out
            i+=1
        return ans
