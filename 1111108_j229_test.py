import random as r
import time as t

s=[]
with open('j229_08.in','w',encoding='utf-8') as tk:
    for i in range(80):         #資料筆數
        s.append([])
        for k in range(500):     #單筆資料數量
            g=r.randint(1,1000000)
            s[-1].append(g)
            tk.write(str(g)+' ')
        tk.write('\n')

with open('j229_08.out','w',encoding='utf-8') as tk:
    tt=t.time()
    for nums in s:
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            for k in range(i):
                if nums[i]>nums[k]:
                    if dp[k]+1>dp[i]:dp[i]=dp[k]+1
        tk.write(str(max(dp))+'\n')
    print(t.time()-tt)