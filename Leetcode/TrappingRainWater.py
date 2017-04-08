class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right=len(height)-1
        res=0
        maxleft=maxright=left=0
        while(left<=right):
            if height[left]<=height[right]:
                if height[left]>=maxleft:
                    maxleft=height[left]
                else:
                    res+=maxleft-height[left]
                left+=1
            else:
                if height[right]>=maxright:
                    maxright=height[right]
                else:
                    res+=maxright-height[right]
                right-=1
        return res