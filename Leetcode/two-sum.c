//
//  two-sum.c
//  
//
//  Created by 雷扬 on 17/3/2.
//
//
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *output;
    output=(int*)malloc(2*sizeof(int));
    int i,j;
    for(i=0;i<numsSize;i++)
    {
        for(j=i+1;j<numsSize;j++)
        {
            if (nums[i]+nums[j]==target)
            {
                output[0]=i;
                output[1]=j;
                return output;
            }
        }
    }
    return output;
}
