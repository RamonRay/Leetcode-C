class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        h=min(height[0],height[n-1])
        ans=0
        while(left<right):
            h=min(height[left],height[right])
            ans=max(ans,h*(right-left))
            while(height[left]<=h and left<right):left+=1
            while(height[right]<=h and left<right):right-=1
        return ans
            
            
