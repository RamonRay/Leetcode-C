//
//  LongestSubString.c
//  
//
//  Created by 雷扬 on 17/3/2.
//
//

int lengthOfLongestSubstring(char* s) {
    char mark[256];
    int size;
    if(*s!=0)
        size=strlen(s);
    else
        return 0;
    int i,j;
    int max=1;
    for(i=0;i<size;i++)
    {
        memset(mark,0,sizeof(mark));
        mark[s[i]]=1;
        for(j=i+1;j<size;j++)
        {
            if(mark[s[j]]==0)
                mark[s[j]]=1;
            else
            {
                if(j-i>max)
                {
                    max=j-i;
                }
                break;
            }
            if(j==size-1)
                if(j-i+1>max)
                    max=j-i+1;
        }
    }
    
    return max;
}
