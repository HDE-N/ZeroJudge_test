import random as r

ss=[1,5,7,10,20,40,1200,5500,8700,18700]
s=[]
with open('j187_09.in','w',encoding='utf-8') as tk:
    for k in range(7):
        for i in ss:tk.write(str(i)+' ')
        tk.write('\n')
        g=r.randint(90000,100000)
        s.append(g)
        tk.write(str(g)+'\n')

with open('j187_09.out','w',encoding='utf-8') as tk:
    for b in s:
        dp=[100001 for x in range(b+1)]
        dp[0]=0
        for i in ss:
            for k in range(i,b+1):
                if dp[k]>dp[k-i]+1:
                    dp[k]=dp[k-i]+1
        if dp[-1]==100001:tk.write('-1\n')
        else:tk.write(str(dp[-1])+'\n')