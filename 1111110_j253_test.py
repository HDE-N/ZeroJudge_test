import random as r

s=[]
a,b=1000,1000     #串列長寬
with open('j254_09.in','w',encoding='utf-8') as tk:
    for i in range(2):                    # i 筆測資
        s.append([])
        tk.write(str(a)+' '+str(b)+'\n')
        for k in range(b):
            s[-1].append([])
            for j in range(a):
                c=r.randint(-100000,100000)        #數字範圍
                tk.write(str(c)+' ')
                s[-1][-1].append(c)
            tk.write('\n')


with open('j254_09.out','w',encoding='utf-8') as tk:
    for grid in s:
        dp=[[0 for x in range(a)] for y in range(b)]
        dp[0][0]=grid[0][0]
        for i in range(b):
            for k in range(a):
                if i!=0 and k!=0:
                    if dp[i-1][k]<dp[i][k-1]:dp[i][k]=dp[i][k-1]
                    else:dp[i][k]=dp[i-1][k]
                    dp[i][k]+=grid[i][k]
                elif i!=0 and k==0:dp[i][k]=dp[i-1][k]+grid[i][k]
                elif i==0 and k!=0:dp[i][k]=dp[i][k-1]+grid[i][k]
        tk.write(str(dp[-1][-1])+'\n')