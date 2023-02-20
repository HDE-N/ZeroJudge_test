import random as r
import time

s=1200
a=[]
b=[]
c=7000
with open('i551_05.in','w',encoding='utf-8') as tk:
    tk.write(str(s)+'\n')
    for i in range(s):
        a.append(r.randint(1,1000))
        b.append(r.randint(1,1000))
    for i in a:tk.write(str(i)+' ')
    tk.write('\n')
    for i in b:tk.write(str(i)+' ')
    tk.write('\n')
    tk.write(str(c)+'\n')


with open('i551_05.out','w',encoding='utf-8') as tk:
    t=time.time()
    dp=[0 for x in range(c+1)]
    for i in range(s):
        for k in range(c,a[i]-1,-1):
            if dp[k-a[i]]+b[i]>dp[k]:
                dp[k]=dp[k-a[i]]+b[i]
    print(time.time()-t)
    tk.write(str(dp[-1]))