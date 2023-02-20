import random as r

a=[]
for ssh in range(1000):
    a.append([])
    for i in range(1000):
        a[ssh].append(r.randint(1,10000000))

with open('j097_07.in','w',encoding='utf-8') as gg:
    for i in a:
        for k in i:
            gg.write(str(k)+' ')
        gg.write('\n')

with open('j097_07.out','w',encoding='utf-8') as gg:
    for ssh in a:
        dp=[0,0]
        for i in range(2,len(ssh)+1):
            if dp[i-1]+ssh[i-1]>dp[i-2]+ssh[i-2]:dp.append(dp[i-2]+ssh[i-2])
            else:dp.append(dp[i-1]+ssh[i-1])
        gg.write(str(dp[-1])+'\n')